+++
date = 2020-08-07T12:50:42Z
description = "С помощью range() и его неожиданных возможностей."
image = "/assets/projects/ohmypy-2.png"
slug = "range"
tags = ["ohmypy"]
title = "Python. Грамотно работать с любым диапазоном"
+++

Все знают, что `range()` в питоне используется, когда нужно что-то сделать сколько-то раз:

```python
>>> for i in range(3, 0, -1):
...   print(i)

3
2
1
```

Но не все знают, что `range` — это коллекция (что? да!), вполне себе полноценная:

```python
>>> seq = range(10, 100)
>>> len(seq)
90
>>> 52 in seq
True
>>> seq[10]
20
```

И даже так:

```python
>>> max(seq)
99
>>> seq.index(31)
21
>>> seq.count(42)
1
```

И так тоже:

```python
>>> s1 = range(0, 10, 3)
>>> s2 = range(0, 11, 3)
>>> s1 == s2
True
```

При этом `range`, в отличие от всех прочих коллекций, занимает мизерное место в памяти (48 байт), вне зависимости от того, сколько элементов в него попадают. Это потому, что хранит он только 3 атрибута: `start`, `stop`, `step`

```python
>>> from pympler import asizeof
>>> seq = range(0, 100)
>>> asizeof.asizeof(seq)
48
>>> seq = range(0, 100_000)
>>> asizeof.asizeof(seq)
48
>>> seq = range(0, 100_000_000)
>>> asizeof.asizeof(seq)
48
```

И при этом идеальное время выполнения операций: `len()`, `[idx]`, `in`, `.index()`, `.count()` — всё за *O(1)*.

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Кто-то на этом месте скажет «погодите, откуда _O(1)_? у списка ведь `in`, `.index()`, `.count()` выполняются за *O(n)*, почему у диапазона иначе?»

Рассмотрим на примере `in`. Действительно: чтобы проверить, есть ли элемент в списке, придётся обходить элементы списка, пока не найдём искомый — это сложность _O(n)_. Но в случае с диапазоном мы точно знаем первый элемент, последний элемент и шаг. Поэтому разработчики стандартной библиотеки пошли на хитрость.

Допустим, есть выражение `x in range(start, stop, step)`. Для положительного step можно обойтись без перебора всех элементов, вот так:

```python
def contains(range_, x):
    if x < range_.start:
        return False
    if x >= range_.stop:
        return False
    return (x - range_.start) % range_.step == 0

>>> r = range(1000, 10000, 3)
>>> contains(r, 2068)
True
>>> contains(r, 2070)
False
```

Проверили границы, посчитали остаток от деления, бумс, готово. Для `.index()` и `.count()` сделано аналогично, если интересно как — посмотрите исходники (осторожно, код на `C`):

-   [range_contains_long](https://github.com/python/cpython/blob/384621c42f9102e31ba2c47feba144af09c989e5/Objects/rangeobject.c#L368)
-   [range_index](https://github.com/python/cpython/blob/384621c42f9102e31ba2c47feba144af09c989e5/Objects/rangeobject.c#L562)
-   [range_count](https://github.com/python/cpython/blob/384621c42f9102e31ba2c47feba144af09c989e5/Objects/rangeobject.c#L544)

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Итого, получили структуру данных постоянного размера, с константным временем выполнения операций. Ну разве он не чудо, этот `range`?

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
