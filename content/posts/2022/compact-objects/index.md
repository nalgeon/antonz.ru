+++
date = 2022-05-13T20:25:00Z
title = "Компактные объекты в Python"
description = "Кортеж против датакласса, пока не вмешается numpy"
image = "/compact-objects/cover.png"
slug = "compact-objects"
tags = ["ohmypy"]
subscribe = "ohmypy"
+++

Питон — объектный язык. Это здорово и удобно, пока не придется создать 10 млн объектов в памяти, которые благополучно ее и съедят. Поговорим о том, как уменьшить аппетит.

Допустим, есть у вас простенький объект «питомец» с атрибутами «имя» (строка) и «стоимость» (целое). Интуитивно кажется, что самое компактное предоставление — в виде кортежа:

```python
("Frank the Pigeon", 50000)
```

Замерим, сколько займет в памяти один такой красавчик:

```python
import random
from pympler.asizeof import asizeof

def fields():
    name_gen = (random.choice(string.ascii_uppercase) for _ in range(10))
    name = "".join(name_gen)
    price = random.randint(10000, 99999)
    return (name, price)

def measure(name, fn, n=10_000):
    pets = [fn() for _ in range(n)]
    size = round(asizeof(pets) / n)
    print(f"Pet size ({name}) = {size} bytes")
    return size

baseline = measure("tuple", fields)
```

```
Pet size (tuple) = 161 bytes
```

161 байт. Будем использовать как основу для сравнения.

С чистыми кортежами, конечно, работать неудобно. Наверняка вы используете датакласс:

```python
from dataclasses import dataclass

@dataclass
class PetData:
    name: str
    price: int

fn = lambda: PetData(*fields())
measure("dataclass", fn)
```

```
Pet size (dataclass) = 257 bytes
x1.60 to baseline
```

Ого, какой толстенький!

Попробуем использовать именованный кортеж:

```python
from typing import NamedTuple

class PetTuple(NamedTuple):
    name: str
    price: int


fn = lambda: PetTuple(*fields())
measure("named tuple", fn)
```

```
Pet size (named tuple) = 161 bytes
x1.00 to baseline
```

Теперь вы понимаете, за что я его [так люблю](/namedtuple/). Удобный интерфейс как у датакласса — а вес как у кортежа. Идеально.

Или нет? В Python 3.10 приехали датаклассы со слотами:

```python
@dataclass(slots=True)
class PetData:
    name: str
    price: int


fn = lambda: PetData(*fields())
measure("dataclass w/slots", fn)
```

```
Pet size (dataclass w/slots) = 153 bytes
x0.95 to baseline
```

Ого! Магия слотов создает специальные худощавые объекты, у которых внутри нет словаря, в отличие от обычных питонячих объектов. И такой датакласс ничуть не уступает кортежу.

Что делать, если 3.10 вам еще не завезли? Использовать `NamedTuple`. Или прописывать слоты вручную:

```python
@dataclass
class PetData:
    __slots__ = ("name", "price")
    name: str
    price: int
```

У слотовых объектов есть свои недостатоки. Но они отлично подходят для простых случаев (без наследования и прочих извращений).

P.S. Конечно, настоящий победитель — numpy-массив. Но с ним неинтересно соревноваться ツ

```python
import string
import numpy as np

PetNumpy = np.dtype([("name", "S10"), ("price", "i4")])
generator = (fields() for _ in range(n))
pets = np.fromiter(generator, dtype=PetNumpy)
size = round(asizeof(pets) / n)
```

```
Pet size (structured array) = 14 bytes
x0.09 to baseline
```

<div class="row">
<div class="col-xs-12 col-sm-4">
<figure><img alt="Кортеж" src="tuple.png"></figure>
</div>
<div class="col-xs-12 col-sm-4">
<figure><img alt="Датакласс" src="dataclass.png"></figure>
</div>
<div class="col-xs-12 col-sm-4">
<figure><img alt="Именованный кортеж" src="named-tuple.png"></figure>
</div>
</div>

<div class="row">
<div class="col-xs-12 col-sm-4">
<figure><img alt="Датакласс со слотами" src="dataclass-slots.png"></figure>
</div>
<div class="col-xs-12 col-sm-4">
<figure><img alt="Ручные слоты" src="manual-slots.png"></figure>
</div>
<div class="col-xs-12 col-sm-4">
<figure><img alt="numpy-массив" src="np-array.png"></figure>
</div>
</div>
