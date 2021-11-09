+++
date = 2021-05-18T09:33:53Z
description = "С помощью functool.partial()"
image = "/assets/projects/ohmypy-2.png"
slug = "functools-partial"
tags = ["ohmypy"]
title = "«Отнаследовать» функцию от существующей в Python"
+++

Допустим, у нас есть список важных гостей. Он в легком беспорядке:

```python
data = [
  "4 - Дуглас",
  "2 - Клер",
  "11 - Зоя",
  "1 - Френк",
  "31 - Питер",
]
```

Отсортируем:

```python
>>> sorted(data)
['1 - Френк', '11 - Зоя', '2 - Клер', '31 - Питер', '4 - Дуглас']
```

Порядка не прибавилось — `sorted()` не знает, что здесь нужна числовая сортировка, а не алфавитная. Поможем ему:

```python
def _key(src):
    parts = src.partition(" - ")
    return int(parts[0])

>>> sorted(data, key=_key)
['1 - Френк', '2 - Клер', '4 - Дуглас', '11 - Зоя', '31 - Питер']
```

Так хорошо! А чтобы добавить семантичности и не таскать везде дополнительный параметр `key`, создадим собственную функцию на основе `sorted()`:

```python
def natsorted(iterable, reverse=False):
    return sorted(iterable, key=_key, reverse=reverse)

>>> natsorted(data)
['1 - Френк', '2 - Клер', '4 - Дуглас', '11 - Зоя', '31 - Питер']
```

Есть и более лакончиный способ сделать это — через `functools.partial()`:

```python
import functools
natsorted = functools.partial(sorted, key=_key)
```

`partial()` создает новую <abbr title="Строго говоря, не функцию, а вызываемый объект, у которого определен дандер call — его можно вызывать, как будто это функция">функцию</abbr> на основе существующей. При этом можно «зафиксировать» один или несколько параметров (мы зафиксировали `key`), разрешив менять остальные (`iterable` и `reverse` в нашем случае).

Таким образом, `partial()` помогает создавать узкоспециализированные функции на базе более универсальных.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>


