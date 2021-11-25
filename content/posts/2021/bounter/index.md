+++
date = 2021-05-30T08:34:00Z
description = "С помощью bounter."
image = "/assets/projects/ohmypy-2.jpg"
slug = "bounter"
tags = ["package", "ohmypy"]
title = "Счетчик для огромных коллекций на Python"
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

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>


