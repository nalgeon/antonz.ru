+++
date = 2022-04-20T21:40:00Z
title = "Закешировать результат вычислений в Python"
description = "С помощью декоратора @functools.lru_cache"
image = "/assets/projects/ohmypy-2.png"
slug = "functools-cache"
tags = ["ohmypy"]
subscribe = "ohmypy"
+++

Предположим, написали вы функцию, которая возвращает емейл пользователя:

```python
def get_user_email(user_id):
    user = find_by_id(user_id)
    return user["email"]
```

Одна беда: функция `find_by_id()` лезет в уж-ж-жасно медленную легаси-систему:

```python
def find_by_id(user_id):
    # представьте здесь медленный запрос по сети,
    # который возвращает пользователя
    time.sleep(1)
    return { "email": "..." }
```

Если 100 раз вызвать `get_user_email(42)` — будет 100 медленных запросов. Хотя по уму хватило бы и одного. Что ж, давайте приделаем простенький кеш:

```python
cache = {}

def get_user_email(user_id):
    if user_id not in cache:
        user = find_by_id(user_id)
        cache[user_id] = user["email"]
    return cache[user_id]
```

Вроде ничего сложного (не считая вопроса устаревания кеша, но об этом в другой раз). Но представьте, что медленных функций много, и в каждую придется приделывать такую штуку. Не слишком вдохновляет.

К счастью, в модуле `functools` есть декоратор `@lru_cache`. Он-то нам и пригодится. Добавляем одну строчку к исходной функции, и готово:

```python
@functools.lru_cache(maxsize=256)
def get_user_email(user_id):
    user = find_by_id(user_id)
    return user["email"]
```

Теперь повторные вызовы `get_user_email()` с одним и тем же `user_id` вернут результат из кеша, не запрашивая `find_by_id()`.

`@lru_cache` прекрасен еще тем, что автоматически вытесняет старые записи из кеша, когда их становится больше `maxsize`. Так что всю память не съест.

В Python 3.9 добавили еще один декоратор — `@functools.cache`. Он такой же как `@lru_cache`, только безразмерный (благодаря чему работает чуть быстрее).

Кешем можно управлять — посмотреть статистику хитов и промахов или почистить.

```python
# управляем кешем

stats = get_user_email.cache_info()
print(stats)
# CacheInfo(hits=2, misses=3, maxsize=256, currsize=3)

get_user_email.cache_clear()
# CacheInfo(hits=0, misses=0, maxsize=256, currsize=0)
```

Работает кеш внутри процесса, и погибнет вместе с ним. Так что если нужно что-то более масштабируемое — посмотрите на Redis или аналоги.

[документация](https://devdocs.io/python/library/functools#functools.lru_cache) •
[песочница](https://replit.com/@antonz/functools-cache#main.py)
