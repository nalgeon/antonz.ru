+++
date = 2021-06-12T17:21:00Z
description = "requests → httpx"
image = "/assets/projects/ohmypy-2.png"
slug = "httpx"
tags = ["package", "ohmypy"]
title = "Современный HTTP-клиент для Python"
subscribe = "ohmypy"
+++

Мало у какого языка такая нажористая стандартная библиотека, как у питона. Но все равно для работы с HTTP люди пользуются сторонним пакетом requests.

А я вот отказался от него в пользу замечательного [**httpx**](https://github.com/encode/httpx/) от Тома Кристи. Синхронный и асинхронный интерфейсы, поддержка wsgi/asgi, плюс все фичи requests — и совместимость с ним!

Можно заменить requests → httpx, и все продолжит работать:

```
>>> import httpx
>>> r = httpx.get("http://httpbingo.org/json")

>>> r.status_code
200

>>> r.headers["content-type"]
'application/json; encoding=utf-8'

>>> r.json()["slideshow"]["title"]
'Sample Slide Show'
```

Питон 3.6+
