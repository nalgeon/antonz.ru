+++
date = 2022-05-15T11:25:00Z
title = "JSON и виртуальные столбцы в SQLite"
description = "Строим NoSQL-базу на минималках."
image = "/json-virtual-columns/cover.png"
slug = "json-virtual-columns"
tags = ["sqlite"]
subscribe = "sqliter"
+++

У [вычисляемых столбцов](/generated-columns/) есть еще одно чрезвычайно полезное применение.

Допустим, вы решили вести журнал событий, которые происходят в системе. События бывают разных типов, у каждого свой набор полей. Например, вход в систему:

```json
{
    "timestamp": "2022-05-15T09:31:00Z",
    "object": "user",
    "object_id": 11,
    "action": "login",
    "details": {
        "ip": "192.168.0.1"
    }
}
```

Или пополнение счета:

```json
{
    "timestamp": "2022-05-15T09:32:00Z",
    "object": "account",
    "object_id": 12,
    "action": "deposit",
    "details": {
        "amount": "1000",
        "currency": "USD"
    }
}
```

Вы решаете не заниматься нормализацией по таблицам, а хранить прямо в JSON. Заводите таблицу `events` с единственным полем `value`:

```sql
select value from events;
```

```
{"timestamp":"2022-05-15T09:31:00Z","object":"user","object_id":11,"action":"login","details":{"ip":"192.168.0.1"}}
{"timestamp":"2022-05-15T09:32:00Z","object":"account","object_id":12,"action":"deposit","details":{"amount":"1000","currency":"USD"}}
{"timestamp":"2022-05-15T09:33:00Z","object":"company","object_id":13,"action":"edit","details":{"fields":["address","phone"]}}
```

И выбираете события по конкретному объекту:

```sql
select
  json_extract(value, '$.object') as object,
  json_extract(value, '$.action') as action
from events
where json_extract(value, '$.object_id') = 11;
```

```
┌────────┬────────┐
│ object │ action │
├────────┼────────┤
│ user   │ login  │
└────────┴────────┘
```

Все здорово, но `json_extract()` при вызове каждый раз парсит текст, так что на сотне тысяч записей запрос будет работать медленно. Что делать?

Создать виртуальные столбцы:

```sql
alter table events
add column object_id integer
as (json_extract(value, '$.object_id'));

alter table events
add column object text
as (json_extract(value, '$.object'));

alter table events
add column action text
as (json_extract(value, '$.action'));
```

Построить индекс:

```sql
create index events_object_id on events(object_id);
```

Теперь запрос работает моментально:

```sql
select object, action
from events
where object_id = 11;
```

Благодаря виртуальным столбцам получилась практически NoSQL база данных ツ

[песочница](https://sqlime.org/#gist:c284f7c22684eb74b5dab92d98f7d773)
