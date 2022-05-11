+++
date = 2019-01-26T15:42:48Z
description = "float.as_integer_ratio() не так прост, как кажется."
image = "/assets/projects/ohmypy-2.png"
slug = "float-as-integer-ratio"
tags = ["ohmypy"]
title = "Python. Из десятичной дроби — в обычную"
subscribe = "ohmypy"
+++

У класса `float` есть прекрасный метод `as_integer_ratio()`, который представляет десятичную дробь в виде обычной — пары «числитель, знаменатель»:

```
>>> (0.25).as_integer_ratio()
(1, 4)

>>> (0.5).as_integer_ratio()
(1, 2)

>>> (0.75).as_integer_ratio()
(3, 4)
```

Так вот. Никогда им не пользуйтесь ツ Потому что:

```
>>> (0.2).as_integer_ratio()
(3602879701896397, 18014398509481984)
```

Виной всему стандарт представления дробных чисел IEEE 754, который реализует float.

Используйте `Decimal`:

```
>>> from decimal import Decimal
>>> Decimal("0.2").as_integer_ratio()
(1, 5)
```

Уверен, вы и так это знаете. Просто на всякий случай ツ
