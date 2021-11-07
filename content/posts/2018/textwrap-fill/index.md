+++
date = 2018-11-29T14:45:00Z
description = "С помощью модуля textwrap."
image = "/assets/projects/ohmypy-2.jpg"
slug = "textwrap-fill"
tags = ["ohmypy"]
title = "Python. Отформатировать текст для консоли"
+++

Если любите делать CLI-утилиты, модуль [textwrap](https://devdocs.io/python/library/textwrap) наверняка вам понравится.

Он умеет перформатировать многострочный текст, чтобы длина строки не превышала N символов:

```
text = "Около двух месяцев назад породистый голубь по имени Френк постучался в стеклянные двери омской ветеринарной клиники"
formatted = textwrap.fill(text, width=20)
print(formatted)

Около двух месяцев
назад породистый
голубь по имени
Френк постучался в
стеклянные двери
```

Или добавить отступ, например для цитаты:

```
import textwrap
inspirational = "Цитаты простых людей:"
quote = "Откройте окно вообще дышать невозможно"
quote = textwrap.indent(quote, prefix="> ")
print(inspirational, quote, sep="\n")

Цитаты простых людей:
> Откройте окно вообще дышать невозможно
```

Френк одобряет.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>

