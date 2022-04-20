+++
date = 2019-01-25T09:06:58Z
description = "С помощью deque(maxlen)."
image = "/assets/projects/ohmypy-2.png"
slug = "deque-maxlen"
tags = ["ohmypy"]
title = "Python. Хранить последние N объектов"
+++

Допустим, вы пишете систему учёта посетителей для музея изящных искусств в Хиросиме (не спрашивайте). Одно из требований безопасников — команда tail, которая показывает трёх последних визитёров. Как её реализовать?

Конечно, можно складывать всех прибывших в список и по запросу выдавать из него последние 3 элемента:

```
TAIL_COUNT = 3
visitors = []

def handle(visitor):
  visitors.append(visitor)

def tail():
  return visitors[-TAIL_COUNT:]

handle("Питер")
handle("Клер")
handle("Френк")
handle("Кен Чан")
handle("Гоу Чан")

>>> visitors
['Питер', 'Клер', 'Френк', 'Кен Чан', 'Гоу Чан']

>>> tail()
['Френк', 'Кен Чан', 'Гоу Чан']
```

Но как-то не очень правильно хранить всех посетителей только ради того, чтобы показывать последних трёх, верно? Нам поможет `collections.deque`:

```
from collections import deque

visitors = deque(maxlen=3)

def handle(visitor):
  visitors.append(visitor)

def tail():
  return list(visitors)

handle("Питер")
handle("Клер")
handle("Френк")
handle("Кен Чан")
handle("Гоу Чан")

>>> visitors
deque(['Френк', 'Кен Чан', 'Гоу Чан'], maxlen=3)

>>> tail()
['Френк', 'Кен Чан', 'Гоу Чан']
```

`deque` (double-ended queue) хранит не более `maxlen` элементов, автоматически «выпихивая» старые при добавлении новых.

А ещё она добавляет элементы в начало и в конец за O(1), в отличие от списка, у которого это O(n). Идеально подходит, если коллекция часто модифицируется, а выбирать элементы по индексу не надо.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
