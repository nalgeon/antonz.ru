+++
date = 2021-06-05T15:00:00Z
description = "С помощью notifiers."
image = "/assets/projects/ohmypy-2.png"
slug = "notifiers"
tags = ["package", "ohmypy"]
title = "Универсальные оповещения на Python"
subscribe = "ohmypy"
+++

Есть куча способов отправлять уведомления — от проверенного SMTP и удобного Telegram до смс и специальных приложений для мобилок вроде Pushover.

Обычно для этого используют 3rd-party библиотеку соответствующего провайдера. Но есть более удобный способ — пакет [**notifiers**](https://github.com/liiight/notifiers) от Ора Карми. Он предоставляет простой универсальный интерфейс для отправки сообщений через любой сервис.

Например, через телеграм:

```python
import notifiers

token = "bot_token"
chat_id = 1234
tg = notifiers.get_notifier("telegram")
tg.notify(message="Привет!", token=token, chat_id=chat_id)
```

Поддерживается аж 16 провайдеров, а интерфейс один — метод `.notify()`. И никаких дополнительных 3rd-party библиотек. Удобно!

Питон 3.6+
