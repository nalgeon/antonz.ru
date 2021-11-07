+++
date = 2021-05-15T08:28:00Z
description = "С помощью natsort."
image = "/assets/projects/ohmypy-2.png"
slug = "natsort"
tags = ["ohmypy", "package"]
title = "Естественная сортировка на Python"
+++

*Это [#пакетик](/tag/package) — еженедельная рубрика о полезных и интересных пакетах на Python.*

Мой сегодняшний выбор — пакет Сета Мортона [**natsort**](https://github.com/SethMMorton/natsort), который сортирует строки привычным для человека образом.

Допустим, у нас есть список важных гостей. Он в легком беспорядке:

```python
data = [
  "4 - Дуглас",
  "2 - Клер",
  "11 - Зоя",
  "1 - Френк",
  "31 - Питер",
]
```

Отсортируем:

```python
>>> sorted(data)
['1 - Френк', '11 - Зоя', '2 - Клер', '31 - Питер', '4 - Дуглас']
```

Порядка не прибавилось ツ А вот как будет с `natsort`:

```python
>>> import natsort
>>> natsort.natsorted(data)
['1 - Френк', '2 - Клер', '4 - Дуглас', '11 - Зоя', '31 - Питер']
```

Другое дело!

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>


