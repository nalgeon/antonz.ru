+++
date = 2018-12-04T15:46:00Z
description = "С помощью pprint.pprint() и аргумента depth."
image = "/assets/projects/ohmypy-2.png"
slug = "pprint-depth"
tags = ["ohmypy"]
title = "Python. Кратко напечатать развесистую структуру"
subscribe = "ohmypy"
+++

Наверняка вы знаете про функции [pprint.pprint()](https://devdocs.io/python/library/pprint#pprint.pprint) и `pprint.pformat()`, которые красиво форматируют разные коллекции и словари.

У них есть замечательный опциональный параметр depth, который ограничивает уровень вложенности при форматировании. Он здорово помогает, если хочется получить общее представление о данных, не сильно вникая в детали.

Например, запросили вы апишечку и получили в ответ развесистый словарь:

```
rating = requests.get("https://www.cia.gov/the-world-factbook/top-dumbest-animals").json()
```

Заглянем в него, не погружаясь в детали:

```
import pprint
pprint.pprint(rating, depth=3)

{'leaderbord': [
  {'details': {...}, 'name': 'Голубь Френк', 'position': 1},
  {'details': {...}, 'name': 'Лисица Клер', 'position': 2},
  {'details': {...}, 'name': 'Попугай Питер', 'position': 3},
  {'details': {...}, 'name': 'Свинка Зои', 'position': 4},
  {'details': {...}, 'name': 'Макака Лукас', 'position': 5}],
 'name': 'Самые тупые животные'}
```

Ненужные подробности автоматически скрыты за «...», и мы видим самую суть. Френк, я в тебе не сомневался.
