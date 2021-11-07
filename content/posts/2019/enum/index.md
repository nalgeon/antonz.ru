+++
date = 2019-01-04T15:31:45Z
description = "Его придумали не просто так."
image = "/assets/projects/ohmypy-2.jpg"
slug = "enum"
tags = ["ohmypy"]
title = "Python. Enum здорового человека"
+++

Если программист привык писать код, как это делали наши пращуры со времён аграрной революции, то перечисления у него выглядят как-то так:

```
class PigeonState:
    eating = 0
    sleeping = 1
    flying = 2

PigeonState.sleeping
1
```

Конечно, у наших современников есть способ получше — [enum.Enum](https://devdocs.io/python~3.7/library/enum):

```
import enum
class PigeonState(enum.Enum):
    eating = 0
    sleeping = 1
    flying = 2

PigeonState.sleeping.value
1
```

Это не просто более многословный способ сделать то же самое. У енумов есть вагон плюшек, недоступных староверам. Например, можно делать синонимы состояний:

```
class PigeonState(enum.Enum):
    eating = 0
    sleeping = 1
    flying = 2
    
    # There is no way Frank is really doing that
    thinking = 1

PigeonState.thinking
<PigeonState.sleeping: 1>
```

Или добавлять свои атрибуты:

```
class PigeonState(enum.Enum):
    eating = (0, "Ест")
    sleeping = (1, "Спит")
    flying = (2, "Парит в небесах")
    
    def __init__(self, id, title):
        self.id = id
        self.title = title

PigeonState.flying.id
2

PigeonState.flying.title
'Парит в небесах'
```

А ещё можно:

- сравнивать по is вместо ==
- сортировать с помощью enum.IntEnum
- итерировать по значениям
- создавать динамически

В общем, енумы — однозначное добро.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>

