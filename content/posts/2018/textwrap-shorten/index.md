+++
date = 2018-11-28T17:46:00Z
description = "С помощью textwrap.shorten()"
image = "/assets/projects/ohmypy-2.png"
slug = "textwrap-shorten"
tags = ["ohmypy"]
title = "Python. Сделать превьюшку длинного текста"
subscribe = "ohmypy"
+++

Допустим, мы хотим получить превьюшку длинной статьи. Можно обрезать механически:

```
article = "Около двух месяцев назад породистый голубь по имени Френк постучался в стеклянные двери омской ветеринарной клиники"
article[:30]

'Около двух месяцев назад пород'
```

Фраза оборвана посреди слова — это неуважение к читателю и к Френку.

А можно воспользоваться функцией [textwrap.shorten()](https://devdocs.io/python/library/textwrap#textwrap.shorten):

```
import textwrap
textwrap.shorten(article, 30, placeholder="...")

'Около двух месяцев назад...'
```

Намного лучше!
