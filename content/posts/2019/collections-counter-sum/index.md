+++
date = 2019-01-19T08:39:13Z
description = "С помощью collections.Counter"
image = "/assets/projects/ohmypy-2.jpg"
slug = "collections-counter-sum"
tags = ["ohmypy"]
title = "Python. Операции со статистикой"
+++

Вернёмся к примеру со статистикой по заявкам разных типов. Вот данные о вопросах, проблемах и идеях за три дня:

```
monday = {"question": 1, "problem": 3, "idea": 2}
tuesday = {"problem": 5, "idea": 1}
wednesday = {"question": 2, "problem": 2}
```

Как бы посчитать агрегированную статистику? Можно так, конечно:

```
def add_day(day_stats, stats):
  for key, value in day_stats.items():
    stats[key] += value
  return stats

stats = {"question": 0, "problem": 0, "idea": 0}
stats = add_day(monday, stats)
stats = add_day(tuesday, stats)
stats = add_day(wednesday, stats)

stats
{'question': 3, 'problem': 10, 'idea': 3}
```

Но вы наверняка догадываетесь, что это не наш метод. Поможет арифметика со счётчиками:

```
from collections import Counter

monday = Counter({"question": 1, "problem": 3, "idea": 2})
tuesday = Counter({"problem": 5, "idea": 1})
wednesday = Counter({"question": 2, "problem": 2})

stats = monday + tuesday + wednesday

stats
Counter({'problem': 10, 'question': 3, 'idea': 3})
```

Что насчёт самого популярного типа заявок?

```
stats.most_common(1)
[('problem', 10)]
```

А какие типы заявок встречались во вторник и в среду?

```
(tuesday | wednesday).keys()
dict_keys(['problem', 'idea', 'question'])
```

А сколько проблем было за все дни кроме понедельника?

```
(stats - monday)["problem"]
7
```

Думаю, вы уловили идею ツ

P.S. Хотите реально злую штуку? Вот как посчитать агрегированную статистику в одну строчку:

```
sum(map(Counter, [monday, tuesday, wednesday]), Counter())
```

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>

