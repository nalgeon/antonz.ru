+++
date = 2021-06-05T15:00:00Z
description = "С помощью notifiers."
image = "/assets/projects/ohmypy-2.png"
slug = "notifiers"
tags = ["package", "ohmypy"]
title = "Универсальные оповещения на Python"
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

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>



