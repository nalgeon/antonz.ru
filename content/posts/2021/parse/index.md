+++
date = 2021-06-19T17:24:59Z
description = "С помощью parse"
image = "/assets/projects/ohmypy-2.png"
slug = "parse"
tags = ["package", "ohmypy"]
title = "Разбор текста по шаблону на Python"
subscribe = "ohmypy"
+++

Все знают, как в питоне форматировать текст по шаблону:

```python
import datetime as dt

date = dt.date(2020, 11, 20)
who = "Френк"
count = 42

tmpl = "{:%Y-%m-%d}: {} и его {:d} друга вылетели в Копенгаген"

>>> tmpl.format(date, who, count)
'2020-11-20: Френк и его 42 друга вылетели в Копенгаген'
```

А благодаря библиотеке [**parse**](https://github.com/r1chardj0n3s/parse) от Ричарда Джонса, с такой же легкостью можно разбирать текст обратно по переменным:

```python
import parse

tmpl = "{:ti}: {} и его {:d} друга вылетели в Копенгаген"
txt = "2020-11-20: Френк и его 42 друга вылетели в Копенгаген"

>>> date, who, count = parse.parse(tmpl, txt)
>>> date
datetime.datetime(2020, 11, 20, 0, 0)
>>> who
'Френк'
>>> count
42
```

parse по большей части поддерживает стандартный питонячий [мини-язык форматирования](https://docs.python.org/3/library/string.html#format-specification-mini-language), так что новый синтаксис учить не придется.

Внутри работает на регулярках. Ноль зависимостей, питон 2 и 3.
