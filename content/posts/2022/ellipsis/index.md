+++
date = 2022-06-03T10:50:00Z
title = "Многозначительное многоточие в Python"
description = "Что такое Ellipsis и как его используют."
image = "/ellipsis/cover.png"
slug = "ellipsis"
tags = ["ohmypy"]
subscribe = "ohmypy"
+++

Не самая известная штука в Python — многоточие:

```python
class Flyer:
    def fly(self):
        ...
```

Это рабочий код. В питоне `...` (он же `Ellipsis`) — реальный объект, который можно использовать в коде.

`Ellipsis` — единственный экземпляр типа `EllipsisType` (аналогично тому, как `None` — единственный экземпляр типа `NoneType`):

```python
>>> ... is Ellipsis
>>> True
>>> Ellipsis is ...
>>> True
```

Авторы Python в основном используют `...`, чтобы показать, что у типа, метода или функции отсутствует реализация — как в примере с `fly()`.

И в [тайп-хинтах](https://docs.python.org/3/library/typing.html):

> It is possible to declare the return type of a callable without specifying the call signature by substituting a literal ellipsis for the list of arguments in the type hint: `Callable[..., ReturnType]`

> To specify a variable-length tuple of homogeneous type, use literal ellipsis, e.g. `Tuple[int, ...]`. A plain `Tuple` is equivalent to `Tuple[Any, ...]`, and in turn to tuple.

```python
# numbers  - кортеж целых чисел произвольной длины
# summator - функция, которая принимает любые аргументы,
#            а возвращает целое число
def print_sum(numbers: tuple[int, ...], summator: Callable[..., int]):
    total = summator(numbers)
    print(total)

print_sum((1, 2, 3), sum)
# 6
```

Ну, а обычные разработчики... Кто во что горазд ツ
