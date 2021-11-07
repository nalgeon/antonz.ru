+++
date = 2021-03-03T13:09:26Z
description = "Математические функции, удаление столбцов и материализованные CTE."
image = "/sqlite-3-35/cover.png"
slug = "sqlite-3-35"
tags = ["sqlite", "data"]
title = "Что нового в SQLite 3.35"
+++

В новых релизах разработчики SQLite часто перебирают движок так и сяк, а для внешнего наблюдателя ничего особо не меняется. 2020 год стал приятным исключением — добавили кучу приятных фич для пользователей, вроде вычисляемых столбцов, `UPDATE FROM` и великолепного `.mode box` в консоли.

Есть все шансы, что 2021 год продолжит традицию. Вот что сделали в релизе 3.35 (вышел 12 марта):

1. Математические функции ‼️
2. Удаление столбцов ❗
3. Возврат обработанных строк для `DELETE`, `INSERT` и `UPDATE` (выражение RETURNING).
4. Материализованные CTE.

Чуть подробнее о каждой фиче:

## Математические функции

Много лет авторов SQLite буквально умоляли добавить базовые функции вроде `sqrt()`, `log()` и `pow()`. Ответ всегда был примерно одинаковый:

> SQLite не просто так называется «lite». Нужны вам функции — добавьте сами.

В целом понятная позиция. Но не добавлять квадратный корень? И при этом реализовать аналитические функции, рекурсивные запросы и прочую продвинутую SQL-магию? Серьезно?

Я подозреваю, что дело в другом, и разработчики SQLite делают те фичи, за которые готовы платить крупные клиенты. Так или иначе, спустя 20 лет у нас появились математические функции!

Вот полный список:

```
acos(X)
acosh(X)
asin(X)
asinh(X)
atan(X)
atan2(X,Y)
ceil(X)
ceiling(X)
cos(X)
cosh(X)
degrees(X)
exp(X)
floor(X)
ln(X)
log(B,X)
log(X)
log10(X)
log2(X)
mod(X,Y)
pi()
pow(X,Y)
power(X,Y)
radians(X)
sin(X)
sinh(X)
sqrt(X)
tan(X)
tanh(X)
trunc(X)
```

## Удаление столбцов

Наверно, второй по популярности источник страданий разработчиков. Невероятно бесит, что можно насоздавать сколько угодно столбцов в таблице, а удалить нельзя. Хочешь удалить столбец — делай копию таблицы без него, а старую удаляй.

Теперь эта боль тоже уйдет! `ALTER TABLE DROP COLUMN`, как долго мы тебя ждали.

Чтобы удалить столбец, SQLite придется полностью перезаписать таблицу — так что операция это небыстрая. Но все равно приятно.

## RETURNING

Из запросов `DELETE`, `INSERT` и `UPDATE` теперь можно возвращать строчки, которые они удалили, добавили или изменили.

Например, можно вернуть идентификатор новой записи:

```sql
create table users (
  id integer primary key,
  first_name text,
  last_name text
);

insert into users (first_name, last_name)
values ('Нина', 'Жукова')
returning id;
```

Или вернуть товары, которым повысили цену:

```sql
update products set price = price * 1.10
where price <= 99.99
returning name, price as new_price;
```

## Материализованные CTE

CTE, или Common Table Expression — отличный способ сделать запрос короче и выразительнее. Например, посчитать количество городов, основанных в каждом столетии:

```
create table city(
  city text,
  timezone text,
  geo_lat real,
  geo_lon real,
  population integer,
  foundation_year integer
);

-- insert data ...

with history as (
  select
    city,
    (foundation_year/100)+1 as century
  from city
)
select
  century || '-й век' as dates,
  count(*) as city_count
from history
group by century
order by century desc;
```

Если одно и то же CTE встречается в запросе несколько раз, SQLite каждый раз его вычисляет. Для больших таблиц это может быть небыстро.

С материализованным CTE SQLite выполнит запрос один раз, запомнит результат, и не будет его пересчитывать (в пределах запроса):

```
with history as materialized (
  select ...
)
select ... from history where ...
except
select ... from history where ...
;
```

<p class="text-centered">⌘&nbsp;⌘&nbsp;⌘</p>

И все это в одном релизе! Невероятно ツ

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>И подписывайтесь на канал <span class="nowrap"><i class="fas fa-database"></i> «<a href="https://t.me/sqliter">SQLite на практике</a>»</span></em></p></div>
</div>



