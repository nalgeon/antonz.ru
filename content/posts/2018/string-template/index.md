+++
date = 2018-12-12T15:32:00Z
description = "С помощью string.Template"
image = "/assets/projects/ohmypy-2.png"
slug = "string-template"
tags = ["ohmypy"]
title = "Python. Шаблонизатор для бедных"
+++

Мантра «There should be one — and preferably only one — obvious way to do it» из Zen of Python далека от реальности.

Все мы знаем, что в Питоне за долгие годы собрали аж три способа подстановки переменных в строку:

```
who = "Голубь Френк"
"%s постучался в стеклянные двери" % who
"{} постучался в стеклянные двери".format(who)
f"{who} постучался в стеклянные двери"
```

Но не все знают, что есть ещё и четвёртый способ — [string.Template](https://devdocs.io/python~3.7/library/string#string.Template). Больше того, он ещё и может быть полезен иногда.

Например, если вам не нужны расширенные возможности вроде форматирования чисел или обращения к атрибутам внутри шаблона, а нужно тупо заменять строковые переменные на их значения. Да ещё и синтаксис подстановки отличается от стандартного:

> CHANGEME:who постучался в стеклянные двери

Тут и пригодится string.Template:

```
import string
class OmskTemplate(string.Template):
    delimiter = "CHANGEME:"

template = OmskTemplate("CHANGEME:who постучался в стеклянные двери")
template.substitute({ "who": "Кот Джарвис"})

'Кот Джарвис постучался в стеклянные двери'
```

Если нужен ещё более извращённый синтаксис — например, `==!who!==` — достаточно перекрыть атрибут класса pattern, указав в нём подходящее регулярное выражение.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
