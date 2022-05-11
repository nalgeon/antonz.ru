+++
date = 2019-06-25T13:15:00Z
description = "С помощью calendar"
image = "/assets/projects/ohmypy-2.png"
slug = "calendar"
tags = ["ohmypy"]
title = "Python. Узнать день недели 40 лет назад"
subscribe = "ohmypy"
+++

Есть в питоне модуль `calendar`. Лично я ожидал от него крутых фич по работе с датами, которые не влезли в `datetime`.

На деле он занимается форматированием календарей в HTML (именно то, что требуется в стандартной библиотеке любого языка) и предоставляет гениальные методы вроде itermonthdays, itermonthdays2, itermonthdays3 и itermonthdays4 (оцените богатство выбора, прямо как на воскресной ярмарке).

Но есть в нём и полезные функции. Например, узнать день недели для любой даты в прошлом или будущем:

```
import calendar
wday = calendar.weekday(1959, 11, 5)

>>> calendar.day_name[wday]
'Thursday'
```

Или вспомнить, сколько дней в июне:

```
import datetime as dt
today = dt.date.today()
_, days = calendar.monthrange(today.year, today.month)

>>> days
30
```

Или проверить, високосный ли год:

```
>>> calendar.isleap(2020)
True
```

А генерировать HTML-календари с помощью `calendar` вы не будете, надеюсь ツ
