+++
date = 2018-12-02T18:05:00Z
description = "С помощью модуля fnmatch."
image = "/assets/projects/ohmypy-2.png"
slug = "fnmatch"
tags = ["ohmypy"]
title = "Python. Простое сравнение с шаблоном"
+++

Для проверки строки по шаблону обычно используют регулярные выражения и модуль `re`. Но иногда хочется что-нибудь попроще, пусть и не такое мощное — вроде like в SQL.

Сравнить строку или список с шаблоном поможет модуль [fnmatch](https://devdocs.io/python~3.7/library/fnmatch):

```
import fnmatch
journal = [
  "10:00 Начался обычный день в омской ветклинике",
  "10:30 Голубь Френк постучался в стеклянные двери",
  "10:50 Лисица Клер поскреблась в окно",
  "11:10 Попугай Питер проник через вентиляцию",
  "11:11 Клер попыталась сожрать Френка и Питера",
  "11:25 Осьминог Пауль всплыл в мужском туалете",
]

fnmatch.filter(journal, "*Френк*")
[ '10:30 Голубь Френк постучался в стеклянные двери',
  '11:11 Клер попыталась сожрать Френка и Питера' ]

fnmatch.fnmatch("frank", "f???k")
True
```

Под капотом используются регулярки, так что всегда можно конвертировать шаблон в регулярное выражение:

```
fnmatch.translate("*Френк*")
'(?s:.*Френк.*)\\Z'
```

Курлык.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>