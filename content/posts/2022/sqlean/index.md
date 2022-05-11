+++
date = 2022-01-04T11:30:00Z
title = "Все расширения для SQLite"
description = "Регулярки, статистика, файлы и еще 100+ функций."
image = "/sqlean/cover.png"
slug = "sqlean"
tags = ["sqlite", "data"]
featured = true
subscribe = "sqliter"
+++

Мне очень нравится SQLite. Это миниатюрная встраиваемая база, которая отлично подходит как для исследовательского анализа данных, так и в качестве хранилища для небольших приложений ([писал об этом](https://habr.com/ru/post/547448/), не буду повторяться).

Но есть у нее один недостаток: маловато встроенных функций по сравнению с PostgreSQL или Oracle. К счастью, авторы заложили в SQLite механизм расширений, на котором можно сделать почти все что угодно. В результате интернет заполнен обрывочными расширениями, которые добавляют функцию-другую.

Мне хотелось большой системности. В результате появился проект **sqlean** — в нем я собираю вместе недостающие в SQLite функции, распределяю их по модулям, рефакторю код, пишу тесты и документацию. Получается что-то вроде стандартной библиотеки, как в Python или Go, только для SQLite.

Я планирую подробно написать про каждый модуль в отдельной статье, а пока — вот краткий обзор.

## Основной набор

Это самые популярные функции, которых не хватало в SQLite:

-   [crypto](https://github.com/nalgeon/sqlean/blob/main/docs/crypto.md): криптографические хеш-функции вроде MD5, SHA-1 и SHA-256.
-   [fileio](https://github.com/nalgeon/sqlean/blob/main/docs/fileio.md): работа с файловой системой — чтение и запись файлов, создание каталогов.
-   [fuzzy](https://github.com/nalgeon/sqlean/blob/main/docs/fuzzy.md): нечеткое сравнение строк, фонетические алгоритмы, транслитерация.
-   [ipaddr](https://github.com/nalgeon/sqlean/blob/main/docs/ipaddr.md): манипуляция IP-адресами и подсетями.
-   [json1](https://github.com/nalgeon/sqlean/blob/main/docs/json1.md): работа с JSON.
-   [math](https://github.com/nalgeon/sqlean/blob/main/docs/math.md): математические функции.
-   [re](https://github.com/nalgeon/sqlean/blob/main/docs/re.md): регулярные выражения.
-   [stats](https://github.com/nalgeon/sqlean/blob/main/docs/stats.md): статистика — медиана, процентили, стандартное отклонение.
-   [text](https://github.com/nalgeon/sqlean/blob/main/docs/text.md): работа со строками.
-   [unicode](https://github.com/nalgeon/sqlean/blob/main/docs/unicode.md): поддержка юникода для функций `upper()`, `lower()` и `LIKE`.
-   [uuid](https://github.com/nalgeon/sqlean/blob/main/docs/uuid.md): генерация уникальных идентификаторов.
-   [vsv](https://github.com/nalgeon/sqlean/blob/main/docs/vsv.md): работа с CSV-файлами как с таблицами базы.

Все расширения можно [скачать](https://github.com/nalgeon/sqlean/releases/latest) для Windows, Linix и macOS.

## Инкубатор

Функции, которые пока не вошли в основной набор. Эти расширения могут быть плохо структурированы, но я их постепенно рефакторю и переношу в основные.

-   [array](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1004109889): работа с массивами (почти как в постгресе).
-   [besttype](https://github.com/nalgeon/sqlean/issues/27#issuecomment-999732640): преобразует строку в подходящий числовой тип.
-   [bloom](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1002267134): быстрый вероятностный способ понять, есть значение в таблице или нет.
-   [cbrt](https://github.com/nalgeon/sqlean/issues/27#issuecomment-996605444): кубический корень из числа.
-   [classifier](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1001239676): бинарный классификатор на логистической регрессии.
-   [compress](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1000937999) и [sqlar](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1000938046): архивация и распаковка данных.
-   [cron](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997427979): проверяет даты по cron-шаблонам.
-   [define](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1004347222): динамически создает скалярные и табличные функции прямо из SQL.
-   [envfuncs](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997423609): читает переменные среды.
-   [eval](https://github.com/nalgeon/sqlean/issues/27#issuecomment-996432840): выполняет произвольные SQL-запросы.
-   [fcmp](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997482625): сравнение и округление десятичных дробей.
-   [isodate](https://github.com/nalgeon/sqlean/issues/27#issuecomment-998138191): дополнительные функции для работы с датами.
-   [math2](https://github.com/nalgeon/sqlean/issues/27#issuecomment-999128539): больше математических функций и битовой арифметики.
-   [pearson](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997417836): корреляция Пирсона между двумя наборами данных.
-   [pivotvtab](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997052157): сводные таблицы.
-   [recsize](https://github.com/nalgeon/sqlean/issues/27#issuecomment-999732907): считает размер записи в таблице.
-   [spellfix](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1002297477): быстрый поиск похожих слов в словаре.
-   [stats2](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1000902666) и [stats3](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1002703581): еще больше матстатистики.
-   [text2](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1003105288): еще больше функций для работы со строками.
-   [uint](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1001232670): натуральная сортировка и сравнение строк, содержащих числа (natsort).
-   [unhex](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997432989): преобразует строку в бинарные данные (обратная операция для `hex()`).
-   [xmltojson](https://github.com/nalgeon/sqlean/issues/27#issuecomment-997018486): преобразует XML в JSON.
-   [zipfile](https://github.com/nalgeon/sqlean/issues/27#issuecomment-1001190336): читает и пишет zip-архивы.

[Голосуйте](https://github.com/nalgeon/sqlean/issues/27) за расширения в инкубаторе! Чем популярнее расширение, тем быстрее оно попадет в основной набор.

Инкубаторные расширения тоже можно [скачать](https://github.com/nalgeon/sqlean/releases/tag/incubator).

## Как подключить расширение

Есть три способа. Если работаете с командной строкой SQLite (`sqlite.exe`):

```sql
sqlite> .load ./stats
sqlite> select median(value) from generate_series(1, 99);
```

Если используете инструмент вроде DB Browser for SQLite, SQLite Expert или DBeaver:

```sql
select load_extension('c:\Users\anton\sqlite\stats.dll');
select median(value) from generate_series(1, 99);
```

Если работаете из Python (в других языках аналогично):

```python
import sqlite3

connection = sqlite3.connect(":memory:")
connection.enable_load_extension(True)
connection.load_extension("./stats.so")
connection.execute("select median(value) from generate_series(1, 99)")
connection.close()
```

## Что дальше

Если почувствуете, что в SQLite вам не хватает какой-то функции — приходите в репозиторий [**sqlean**](https://github.com/nalgeon/sqlean), там наверняка найдется.

Я продолжаю добавлять новые расширения в инкубатор, а расширения из инкубатора рефакторю и переношу в основные. По каждому основному модулю планирую написать отдельную статью с примерами.

А если захотите поучаствовать — присылайте [свои](https://github.com/nalgeon/sqlean/blob/incubator/docs/submit.md) или [чужие](https://github.com/nalgeon/sqlean/blob/incubator/docs/external.md) расширения.

Всем SQLite!
