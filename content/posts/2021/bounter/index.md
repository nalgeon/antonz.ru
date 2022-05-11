+++
date = 2021-05-30T08:34:00Z
description = "С помощью bounter."
image = "/assets/projects/ohmypy-2.png"
slug = "bounter"
tags = ["package", "ohmypy"]
title = "Счетчик для огромных коллекций на Python"
subscribe = "ohmypy"
+++

В стандартной библиотеке есть класс Counter. Он отлично подходит, чтобы считать [количество объектов разных типов](/collections-counter/). Но что делать, если объектов миллиарды, и счетчик просто не помещается в оперативную память?

Поможет [**bounter**](https://github.com/RaRe-Technologies/bounter) — это счетчик, который предоставляет схожий интерфейс, но внутри построен на вероятностных структурах данных. За счет этого он занимает в 30–250 раз меньше памяти, но может (слегка) привирать.

```python
from bounter import bounter
counts = bounter(size_mb=128)
counts.update(["a", "b", "c", "a", "b"])

>>> counts.total()
5

>>> counts["a"]
2
```

Ноль зависимостей, питон 3.3+
