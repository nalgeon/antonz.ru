+++
date = 2018-12-03T12:06:00Z
description = "С помощью модуля difflib."
image = "/assets/projects/ohmypy-2.png"
slug = "difflib-ratio"
tags = ["ohmypy"]
title = "Python. Сравнить строки на похожесть"
subscribe = "ohmypy"
+++

Помните ваш [стартап с самыми актуальными новостями дня](/string-capwords/)? Кажется, у него появился конкурент — он нагло крадёт ваши аутентичные новости, рерайтит их, и рассылает ничего не подозревающим клиентам, подрывая вашу репутацию.

Судите сами, вот ваши новости:

```
genuine = [
  "«Братец-хлеб» из Китая носит плащ и корону из булочек, чтобы кормить чаек",
  "Мясо гигантских тараканов станет вкусной и недорогой альтернативой говядине",
  "Скандал в ботаническом саду: 10 миллионов рублей ушло на зарплату кактусам",
]
```

А вот новости жалкого подражателя:

```
plagiary = [
  "Китайский хлебный братец кормит чаек плащом и короной из булочек",
  "Гигантское мясо тараканов станет говядине недорогой и вкусной альтернативой",
  "Зарплата кактусов в ботаническом саду составила 10 скандальных миллионов рублей",
]
```

Нужны какие-то основания для судебного иска, и нужны быстро. Хорошо, что в стандартной библиотеке Питона есть модуль [difflib](https://devdocs.io/python~3.7/library/difflib). Сделаем на нём функцию сравнения:

```
import difflib

def similarity(s1, s2):
  normalized1 = s1.lower()
  normalized2 = s2.lower()
  matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
  return matcher.ratio()
```

И сравним:

```
similarity(genuine[0], plagiary[0])
0.51

similarity(genuine[1], plagiary[1])
0.69

similarity(genuine[2], plagiary[2])
0.55
```

АГА! 51%, 69% и 55% похожести! Всё ясно, какие ещё нужны доказательства.
