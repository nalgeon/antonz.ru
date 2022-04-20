+++
date = 2019-01-09T13:17:14Z
description = "С помощью collections.defaultdict или  collections.Counter"
image = "/assets/projects/ohmypy-2.png"
slug = "collections-counter"
tags = ["ohmypy"]
title = "Python. Посчитать количество объектов каждого типа"
+++

Допустим, вы пишете программу, которая обрабатывает заявки разных типов — идеи, вопросы и проблемы:

```
from collections import namedtuple
Request = namedtuple("Request", ("type", "text"))

requests = [
  Request(type="question", text="Как пасти котов?"),
  Request(type="problem", text="Бакланы портят стадион"),
  Request(type="idea", text="Переводчик с лисьего на русский"),
  Request(type="problem", text="Кот крадёт электричество"),
  Request(type="problem", text="Мыши похитили 540 кг марихуаны"),
  Request(type="idea", text="Холодильник с таймером"),
]
```

Предположим, требуется посчитать количество заявок каждого типа. Если в прошлой жизни человек писал на джаваскрипте, код может получиться таким:

```
stats = {}
for req in requests:
  if req.type in stats:
    stats[req.type] += 1
  else:
    stats[req.type] = 1

stats
{'question': 1, 'problem': 3, 'idea': 2}
```

Прямо больно смотреть на этот if, верно? Лучше воспользоваться методом `dict.setdefault()`. Но как по мне, он тоже уродливый, поэтому ещё лучше — [collections.defaultdict](https://devdocs.io/python/library/collections#collections.defaultdict):

```
from collections import defaultdict
stats = defaultdict(lambda: 0)
for req in requests:
    stats[req.type] += 1

dict(stats)
{'question': 1, 'problem': 3, 'idea': 2}
```

А совсем хорошо — [collections.Counter](https://devdocs.io/python/library/collections#collections.Counter):

```
from collections import Counter
stats = Counter(req.type for req in requests)

dict(stats)
{'question': 1, 'problem': 3, 'idea': 2}
```

У счётчиков есть ещё пара полезных особенностей, но о них в другой раз.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
