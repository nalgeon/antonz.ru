+++
date = 2021-02-11T13:34:09Z
description = "Если проект живет на GitHub, настройте за 10 минут авто-сборку под Windows, Linux и macOS."
image = "/github-actions/cover.png"
slug = "github-actions"
tags = ["development"]
title = "Кросс-платформенная сборка с GitHub Actions"
+++

Если проект живет на GitHub, можно за десять минут настроить авто-сборку под основные операционные системы — Windows, Linux и macOS.

Раньше для сборки почти всегда использовали [Travis CI](https://travis-ci.org/), многие по инерции и сейчас так делают. Но есть способ лучше — [GitHub Actions](https://github.com/features/actions).

GitHub Actions — невероятно мощный бесплатный сервис автоматизации любых задач. Грубо говоря, вы выполняете свой код на серверах Гитхаба и делаете там все, что заблагорассудится. Звучит диковато, но открывает бездну возможностей. В том числе — автоматическую сборку проекта под все ОС. Особенно приятно, что можно собирать под Windows.

Вот как это работает:

1. Создаете файл конфигурации.

```
mkdir -p .github/workflows
touch .github/workflows/build.yml
```

2. Указываете условия запуска сборки.

Например, собирать при каждом коммите:

```yaml
on: push
```

Или только из новых тегов:

```yaml
on:
  push:
    tags:
      - "*"
```

3. Перечисляете операционные системы.

```yaml
runs-on: ${{ matrix.os }}
strategy:
  matrix:
    include:
      - os: ubuntu-latest
      - os: windows-latest
      - os: macos-latest
```

4. Указываете шаги сборки.

```yaml
- uses: actions/checkout@v2

- name: Build for Linux
  if: matrix.os == 'ubuntu-latest'
  run: gcc -fPIC -lm -shared src/stats.c -o dist/sqlite3-stats.so

- name: Build for Windows
  if: matrix.os == 'windows-latest'
  run: gcc -fPIC -lm -shared src/stats.c -o dist/sqlite3-stats.dll

- name: Build for macOS
  if: matrix.os == 'macos-latest'
  run: gcc -fno-common -dynamiclib src/stats.c -o dist/sqlite3-stats.dylib
```

Действие `actions/checkout` скачивает исходники, а на остальных шагах выполняются те команды, что указаны по тексту. В примере это сборка исходного кода на C с помощью `gcc`, но у вашего проекта может быть `npm run` для JS или `tox` для Python — то, что обычно используете для сборки.

Если для вашего языка есть стандартный репозиторий пакетов вроде `npm` или `pypi` — здесь же можно опубликовать сборку. Если репозитория нет, можно опубликовать прямо на гитхабе с помощью действия `svenstaro/upload-release-action`:

```yaml
- name: Upload binaries to release
  uses: svenstaro/upload-release-action@v2
  with:
    repo_token: ${{ secrets.GITHUB_TOKEN }}
    file: dist/${{ matrix.artifact_name }}
    asset_name: ${{ matrix.asset_name }}
    tag: ${{ github.ref }}
```

- [Полный пример конфигурации](https://github.com/nalgeon/sqlite-stats/blob/main/.github/workflows/build.yml)

5. Коммитите изменения, пушите и наблюдаете результат на вкладке *Actions* репозитория на Гитхабе.

<p class="text-centered">⌘&nbsp;⌘&nbsp;⌘</p>

Готово! Теперь Гитхаб трудится, а вы отдыхаете.

Еще почитать:

- [Документация по GitHub Actions](https://docs.github.com/en/actions)
- [Как сделать все что угодно вообще с GitHub Actions](https://docs.github.com/en/actions)

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>И подписывайтесь на канал <span class="nowrap"><i class="fas fa-database"></i> «<a href="https://t.me/sqliter">SQLite на практике</a>»</span></em></p></div>
</div>



