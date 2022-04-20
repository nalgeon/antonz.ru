+++
date = 2019-02-18T13:35:18Z
description = "С помощью модуля heapq"
image = "/assets/projects/ohmypy-2.png"
slug = "heapq"
tags = ["ohmypy"]
title = "Python. Обработать заявки с учётом приоритетов"
+++

Если система обрабатывает заявки, редко бывает, что все они одинакового веса. Чаще встречаются разные приоритеты: клиенты бывают обычные и VIP, баги бывают минорные и критические, заказы бывают «до 1000 ₽» и «10000+ ₽».

Если приоритетов нет, обслуживать заявки просто: кто раньше пришёл, того раньше и обслужили (first in, first out — FIFO). С приоритетами сложнее: более важные заявки должны идти вперёд, но среди заявок с одинаковым приоритетом по-прежнему должен действовать принцип FIFO.

Допустим, была у нас система без приоритетов:

```python
from collections import deque

def process(requests):
    while requests:
        client, task = requests.pop()
        print(f"{client}: {task}")

requests = deque()
requests.appendleft(("Лукас", "нарвать бананов"))
requests.appendleft(("Зоя", "почесать спинку"))
requests.appendleft(("Френк", "насыпать зёрен"))

>>> process(requests)
Лукас: нарвать бананов
Зоя: почесать спинку
Френк: насыпать зёрен
```

Обработка по порядку, всё честно. А теперь допустим, что у заявки появился вес:

-   → Лукас, вес 1
-   → Зоя, вес 1
-   → Френк, вес 10

Френк с весом 10 должен пойти первым. А Зоя и Лукас — после него, в порядке поступления: сначала Лукас, потом Зоя.

Реализовать эту логику поможет модуль `heapq`:

```python
import heapq
import time
requests = []

heapq.heappush(requests,
  (-1, time.time_ns(), "Лукас"))
heapq.heappush(requests,
  (-1, time.time_ns(), "Зоя"))
heapq.heappush(requests,
  (-10, time.time_ns(), "Френк"))
```

Здесь первым аргументом мы передаём вес заявки. `heapq.heappush()` ставит первыми элементы с *меньшим* значением, так что берём вес со знаком минус.

Вторым аргументом передаём текущее время в наносекундах, чтобы заявки с одинаковым весом разрешались в порядке поступления.

Проверим результат:

```python
def process(requests):
    while requests:
        _, _, client = heapq.heappop(requests)
        print(f"{client}")

>>> process(requests)
Френк
Лукас
Зоя
```

Порядок!

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
