+++
date = 2019-06-26T16:44:00Z
description = "С помощью bisect.bisect()"
image = "/assets/projects/ohmypy-2.png"
slug = "bisect"
tags = ["ohmypy"]
title = "Python. Быстро найти элемент коллекции"
subscribe = "ohmypy"
+++

Френк решил открыть магазин диковинок. Прайс-лист огромный, приведу только несколько позиций:

```python
from collections import namedtuple
Product = namedtuple("Product", ("price", "name"))

products = [
  Product(1500, "живой багет"),
  Product(3300, "мельница для сыра"),
  Product(6500, "костюм картошки"),
  Product(9900, "беспилотная сова"),
]
```

Магазин открылся, торговля идёт бойко, но есть проблемка. Покупатели донимают вопросом «у меня есть X рублей, какую самую дорогую дичь я могу купить за эту сумму?».

Френк очень плохо считает (неудивительно для голубя), поэтому требуется наша помощь. Давайте сначала решим «в лоб»:

```python
def suggest(max_price):
    best_product = Product(0, None)
    for product in products:
        if product.price > max_price:
            continue
        if product.price > best_product.price:
            best_product = product
    if best_product.name is None:
        return None
    return best_product

>>> suggest(5000)
Product(price=3300, name='мельница для сыра')
```

Работает как часы! Только Френк жалуется, что `suggest()` что-то долго думает (прайс-лист огромный, помните?). Это неудивительно, мы ведь каждый раз перебираем все товары — сложность алгоритма `O(n)`

Надо бы отсортировать товары по цене и использовать алгоритм бинарного поиска, который работает за `O(log n)`. Правда, не слишком греет перспектива реализации алгоритма — Френк требует сделать всё сию же секунду.

Нам поможет модуль `bisect` стандартной библиотеки:

```python
import bisect

prices = sorted(p.price for p in products)

def suggest(max_price):
    best_index = bisect.bisect(prices, max_price)
    if best_index == 0:
        return None
    return products[best_index - 1]

>>> suggest(5000)
Product(price=3300, name='мельница для сыра')
```

Работает так:

-   Создали отсортированный список цен.
-   Покупатель принёс 5000₽ денег.
-   `bisect.bisect()` определил, на какую позицию списка можно вставить 5000, чтобы список остался отсортированным (третья позиция, между 3300 и 6500).
-   Элемент слева от этой позиции и есть интересующий нас товар («мельница» за 3300).

Френк доволен.
