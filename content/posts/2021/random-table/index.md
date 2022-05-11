+++
date = 2021-01-26T10:44:34Z
description = "С помощью рекурсивного селекта WITH RECURSIVE."
image = "/assets/projects/sql.png"
slug = "random-table"
tags = ["sqlite", "data"]
title = "Как создать таблицу на 1М записей одним запросом"
subscribe = "sqliter"
+++

Допустим, вы хотите проверить, как поведет себя запрос на большой таблице — но такой таблицы под рукой нет. Если СУБД умеет в рекурсию, это не проблема: кучу данных можно нагенерить одним запросом. Поможет в этом конструкция `WITH RECURSIVE`.

Я буду использовать SQLite, но похожие запросы сработают в PostgreSQL и других СУБД. `WITH RECURSIVE` поддерживается в MariaDB 10.2+, MySQL 8.0+, PostgreSQL 8.4+ и SQLite 3.8+. Oracle 11.2+ и SQL Server 2005+ поддерживают рекурсивные запросы, но без ключевого слова `RECURSIVE`.

## Случайные числа

Создадим таблицу на 1 млн случайных чисел:

```
create table random_data as
with recursive tmp(x) as (
    select random()
    union all
    select random() from tmp
    limit 1000000
)
select * from tmp;
```

Или, если ваша база поддерживает `generate_series()` (и не поддерживает `limit` в рекурсивных запросах, как PostgreSQL):

```
create table random_data as
select random() as x
from generate_series(1, 1000000);
```

Проверим:

```
sqlite> select count(*) from random_data;
1000000

sqlite> select avg(x) from random_data;
1.000501737529e+16
```

## Числовая последовательность

Вместо случайных чисел заполним таблицу числами от единицы до миллиона:

```
create table seq_data as
with recursive tmp(x) as (
    select 1
    union all
    select x+1 from tmp
    limit 1000000
)
select * from tmp;
```

Или через `generate_series()`:

```
create table seq_data as
select value as x
from generate_series(1, 1000000);
```

Проверим:

```
sqlite> select count(*) from seq_data;
1000000

sqlite> select avg(x) from seq_data;
500000.5

sqlite> select min(x) from seq_data;
1

sqlite> select max(x) from seq_data;
1000000
```

## Рандомизированные данные

Числа — это хорошо, но что, если нужна большая табличка с данными о клиентах? Запросто!

Договоримся о правилах:

- у клиента есть идентификатор, имя и возраст;
- идентификатор заполняем последовательно от 1 до 1000000;
- имя случайным образом выбираем из фиксированного списка;
- возраст берем случайный от 1 до 80.

Создадим таблицу с именами:

```
create table names (
    id integer primary key,
    name text
);

insert into names(id, name)
values
(1, 'Анна'),
(2, 'Борис'),
(3, 'Вера'),
(4, 'Галина'),
(5, 'Денис');
```

И нагенерим клиентов:

```
create table person_data as
with recursive tmp(id, idx, name, age) as (
    select 1, 1, 'Анна', 20
    union all
    select
        tmp.id + 1 as id,
        abs(random() % 5) + 1 as idx,
        (select name from names where id = idx) as name,
        abs(random() % 80) + 1 as age
    from tmp
    limit 1000000
)
select id, name, age from tmp;
```

Или через `generate_series()`:

```
create table person_data as
with tmp as (
    select
        value as id,
        abs(random() % 5) + 1 as idx,
        abs(random() % 80) + 1 as age
    from generate_series(1, 1000000)
)
select
    id,
    (select name from names where id = idx) as name,
    age
from tmp;
```

Здесь все по правилам:

- идентификатор рассчитывается как предыдущее значение + 1;
- поле `idx` содержит случайное число от 1 до 5;
- имя выбирается из таблицы `names` по значению `idx`;
- возраст рассчитывается как случайное число от 1 до 80.

Проверим:

```
sqlite> select count(*) from person_data;
1000000

sqlite> select * from person_data limit 10;
┌────┬───────┬─────┐
│ id │ name  │ age │
├────┼───────┼─────┤
│ 1  │ Анна  │ 20  │
│ 2  │ Анна  │ 76  │
│ 3  │ Борис │ 25  │
│ 4  │ Борис │ 19  │
│ 5  │ Борис │ 11  │
│ 6  │ Вера  │ 72  │
│ 7  │ Анна  │ 41  │
│ 8  │ Денис │ 9   │
│ 9  │ Денис │ 38  │
│ 10 │ Вера  │ 41  │
└────┴───────┴─────┘
```

Миллион клиентов одним запросом, неплохо! Вот бы в продажах так ツ

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Если хотите узнать больше о рекурсивных SQL-запросах, прикладном анализе данных и SQLite — записывайтесь на курс:

<p class="big">
<a href="/sqlite-course/">SQLite для аналитики</a>
</p>

Курс расскажет, как использовать SQLite для повседневной работы с данными. Без воды, куча примеров, применяйте в работе с первого дня.
