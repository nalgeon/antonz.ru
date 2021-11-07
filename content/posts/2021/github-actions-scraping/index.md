+++
date = 2021-03-12T14:12:59Z
description = "Как собрать данные из API, опубликовать датасет на гитхабе и автоматически актуализировать."
image = "/github-actions-scraping/cover.png"
slug = "github-actions-scraping"
tags = ["development", "sqlite"]
title = "Собираем открытые данные с GitHub Actions"
+++

GitHub Actions чаще всего используют для сборки и тестов, но вообще сервис подходит для любой автоматизации.

В этой заметке я расскажу:

- как собрать данные из API,
- опубликовать датасет на гитхабе,
- и автоматически актуализировать.

В результате получится идеальный инструмент для сбора и публикации открытых данных.

Будем работать с API станций метро, которое предоставляет [HeadHunter](https://github.com/hhru/api). Я буду приводить фрагменты конфига для GitHub Actions, а в конце дам ссылку на готовый репозиторий. Поехали!

## 1. Собрать данные из API

Получаем сырой JSON от API, красиво форматируем, сохраняем в файл:

```yaml
- name: Fetch latest data
  run: |-
      curl https://api.hh.ru/metro | jq --indent 4 . > data/metro.json
```

## 2. Опубликовать датасет на гитхабе

Коммитим от имени специального пользователя `actions@users.noreply.github.com` — его можно использовать в сценариях GitHub Actions:

```yaml
- name: Commit and push if changed
  run: |-
      git config user.name "Automated"
      git config user.email "actions@users.noreply.github.com"
      git add -A
      timestamp=$(date --rfc-3339=seconds --utc)
      git commit -m "Latest data: ${timestamp}" || exit 0
      git push
```

Бонусом получаем автоматическую проверку, изменились ли данные с предыдущего запуска. Если не изменились, команда `git add -A` ничего не добавит, и коммит не произойдет. Таким образом, новая версия датасета опубликуется, только если есть изменения.

## 3. Автоматически актуализировать

Сценарий запускается по расписанию, как указано в cron-выражении. Здесь — в 23:00 UTC каждый день:

```yaml
on:
    push:
    workflow_dispatch:
    schedule:
        - cron: "00 23 * * *"
```

## 4. Бонус: JSON → CSV

JSON — это замечательно, но неплохо бы публиковать датасет еще и в CSV. В этом поможет SQLite, который умеет нативно работать с JSON.

Создаем таблицу:

```sql
create table city (
    id text,
    name text,
    url text,
    fullkey
);
```

Загружаем данные из JSON:

```sql
insert into city (id, name, url, fullkey)
select
   json_extract(value, '$.id') as id,
   json_extract(value, '$.name') as name,
   json_extract(value, '$.url') as url,
   fullkey
from json_tree(readfile('data/metro.json'))
where path = '$' and type = 'object';
```

Выгружаем в CSV:

```sql
.mode csv
.headers on
.once data/city.csv
select id, name from city;
```

Сохраняем команды в файл и запускаем в сценарии:

```yaml
- name: Convert json to csv
  run: |-
      sqlite3 -batch data/metro.db < json-to-csv.sql
```

<p class="text-centered">⌘ ⌘ ⌘</p>

Набор данных в трех форматах (JSON, CSV, SQLite) — готов! А теперь попробуйте на своем датасете ツ

[Полный сценарий](https://github.com/nalgeon/metro/blob/main/.github/workflows/scrape.yaml)

[Репозиторий с данными](https://github.com/nalgeon/metro)

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>И подписывайтесь на канал <span class="nowrap"><i class="fas fa-database"></i> «<a href="https://t.me/sqliter">SQLite на практике</a>»</span></em></p></div>
</div>



