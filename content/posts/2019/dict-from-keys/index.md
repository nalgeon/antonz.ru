+++
date = 2019-07-09T14:07:20Z
description = "С помощью dict.from_keys()"
image = "/assets/projects/ohmypy-2.png"
slug = "dict-from-keys"
tags = ["ohmypy"]
title = "Python. Создать словарь по списку ключей"
+++

Предположим, вы сделали робота для общественных пространств. Он будет помогать людям.

Вы решаете, что полезно собирать статистику добрых дел — что и сколько раз робот сделал. Для этого удобно использовать счётчик, ключами которого будут названия действий, а значениями — количество выполнений.

Робот постоянно учится новым полезным активностям, так что набор дел не фиксированный. Он хранится в списке:

```python
actions = [
  "махать флагом",
  "чесать котов",
  "смешить детей",
  "рвать шаблоны",
]
```

Как бы из этого списка сделать счётчик? Так не надо, конечно:

```python
from collections import Counter

counter = Counter()
for action in actions:
    counter[action] = 0

>>> counter

Counter({
  'махать флагом': 0,
  'чесать котов': 0,
  'смешить детей': 0,
  'рвать шаблоны': 0})
```

Намного роднее воспользоваться dictionary comprehension (простите, что на англ — непереводимая игра слов):

```python
counter = Counter({action: 0 for action in actions})
```

Или малоизвестным методом <code>dict.fromkeys()</code>:

```python
counter = Counter(dict.fromkeys(actions, 0))
```

Первый аргумент — список ключей, второй — умолчательное значение. Удобно, а?

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="http://ohmypy.ru">Oh My Py</a>»</span></em></p></div>
</div>
