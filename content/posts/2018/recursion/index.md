+++
date = 2018-08-11T09:51:13Z
description = "Раз и навсегда."
image = "/recursion/cover.png"
slug = "recursion"
tags = ["development"]
title = "Как понять рекурсию"
subscribe = "ohmypy"
+++

У программистов есть расхожая шутка:

> Чтобы понять рекурсию, надо понять рекурсию.

Шутка на самом деле неудачная. Чтобы это увидеть, достаточно перевести её в псевдокод:

```
def understand_recursion():
    understand_recursion()
```

Не хватает важнейшей составляющей — базового случая. В результате получается бесконечная цепочка вызовов. Понятно теперь, почему программисты так лажают в рекурсивных алгоритмах.

Исправим ошибку:

```
def understand_recursion(myself):
    if recursion_is_understood(myself):
        return
    understand_recursion(myself)
```

Или, переходя на естественный язык:

<blockquote class="big">
Чтобы понять рекурсию, надо понимать рекурсию до тех пор, пока не поймёте
</blockquote>
