+++
date = 2019-01-08T12:30:01Z
description = "С помощью collections.ChainMap"
image = "/assets/projects/ohmypy-2.png"
slug = "collections-chainmap"
tags = ["ohmypy"]
title = "Python. Умолчательные значения настроек"
+++

Если в программе есть настройки, хорошо предусмотреть для них умолчательные значения. Так всё будет работать «из коробки», а в конфиг полезут только те, кому это действительно надо.

Допустим, настройки по умолчанию мы сложили в словарь:

```
DEFAULTS = {
  "name": "Frank",
  "species": "pigeon",
  "age": 42,
}
```

А пользовательские настройки лежат в settings.ini. Их можно считать функцией load_settings(), которая тоже возвращает словарь.

Вопрос: как получить актуальное значение того или иного свойства?

Так себе способ:

```
custom = load_settings()

def get_setting_value(name):
  if name in custom:
    return custom[name]
  else:
    return DEFAULTS[name]
```

Способ лучше — воспользоваться [collections.ChainMap](https://devdocs.io/python/library/collections#collections.ChainMap):

```
from collections import ChainMap

# пусть custom ==
# { "species": "human" }
custom = load_settings()
settings = ChainMap(custom, DEFAULTS)

def get_setting_value(name):
  return settings[name]

get_setting_value("name")
'Frank'

get_setting_value("species")
'human'
```

В ChainMap можно запихать сколько угодно словарей, поиск по ним производится последовательно. Присваивание тоже работает:

```
settings["age"] = 33

custom
{'species': 'human', 'age': 33}

DEFAULTS
{'name': 'Frank', 'species': 'pigeon', 'age': 42}
```

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Заметка из телеграм-канала <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>
