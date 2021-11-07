+++
date = 2018-12-07T15:55:00Z
description = "С помощью shlex.split()"
image = "/assets/projects/ohmypy-2.jpg"
slug = "shlex-split"
tags = ["ohmypy"]
title = "Python. Разбить строку на слова с учётом кавычек"
+++

Предположим, вы собираете архив статей, и хотите для каждой автоматически определять теги — по ним можно будет моментально найти статью в архиве. В качестве тегов решили брать топ-3 слова из текста.

Например, такая статья:

```
text = """Голубь Френк прибыл в отель "Четыре сезона" с дружеским визитом. По сообщениям очевидцев, он сожрал в ресторане киноа прямо из тарелки гостя, а затем клюнул в глаз прибежавшего на шум официанта.

Френк прилетает в "Четыре сезона" каждый год. В прошлый раз мерзкая птица нагадила в ванну с шампанским в королевском люксе, лишив кого-то романтического вечера."""
```

Вы чистите текст от пунктуации, бьёте по пробелам и считаете слова. Вот топ-3:

```
[('френк', 2),
 ('четыре', 2),
 ('сезона', 2)]
 ```

Но погодите, разве правильно считать «четыре» и «сезона» разными тегами? Это ведь название отеля, лучше учитывать их как одно словосочетание. Тут-то и пригодится функция [shlex.split()](https://devdocs.io/python/library/shlex#shlex.split) — она трактует словосочетания в кавычках как один токен:

```
# слегка чистим text, для краткости опускаю
import shlex
from collections import Counter

words = shlex.split(text)
words = [word for word in words if len(word) > 3]
Counter(words).most_common(3)

[('френк', 2),
 ('четыре сезона', 2),
 ('голубь', 1)]
```

Вот теперь теги что надо!

P.S. Вообще, shlex предназначен для разбора shell-подобных строк, так что если злая судьба заставит вас парсить bash-скрипты — вы знаете, куда смотреть.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
