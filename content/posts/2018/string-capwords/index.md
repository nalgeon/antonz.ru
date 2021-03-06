+++
date = 2018-11-30T16:01:00Z
description = "С помощью string.capwords()"
image = "/assets/projects/ohmypy-2.png"
slug = "string-capwords"
tags = ["ohmypy"]
title = "Python. Все слова с прописной буквы"
subscribe = "ohmypy"
+++

Допустим, запустили вы стартап. В автоматическом режиме собираете самые упоротые новости русскоязычных СМИ, вот такие:

> Кот из Новокузнецка признан виновным в потопе

Автоматически же переводите их на английский, вот так:

> Cat from Novokuznetsk found guilty in the flood

И ежедневно рассылаете подписчикам по всему миру.

Всё хорошо, но знакомый эксперт из МГИМО подсказывает: в английском принято каждое слово в заголовке начинать с заглавной буквы. А у вас-то не так!

Можно, конечно, бить заголовок по пробелам через `.split()`, исправлять регистр через `.capitalize()` и склеивать обратно через `.join()`. Но есть способ лучше — [string.capwords()](https://devdocs.io/python~3.7/library/string#string.capwords):

```
import string
header = "Cat from Novokuznetsk found guilty in the flood"
string.capwords(header)

'Cat From Novokuznetsk Found Guilty In The Flood'
```

Соу мач беттер.
