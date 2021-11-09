+++
date = 2019-02-01T11:52:24Z
description = "С помощью collections.namedtuple"
image = "/assets/projects/ohmypy-2.jpg"
slug = "namedtuple"
tags = ["ohmypy"]
title = "Python. Кортеж здорового человека"
+++

Эта статья — об одном из лучших изобретений Python: именованном кортеже (namedtuple). Мы рассмотрим его приятные особенности, от известных до неочевидных. Уровень погружения в тему будет нарастать постепенно, так что, надеюсь, каждый найдёт для себя что-то интересное. Поехали!

## Введение

Наверняка вы сталкивались с ситуацией, когда нужно передать несколько свойств объекта одним куском. Например, информацию о домашнем питомце: тип, кличка и возраст.

Часто создавать отдельный класс под это дело лень, и используют кортежи:

```python
("pigeon", "Френк", 3)
("fox", "Клер", 7)
("parrot", "Питер", 1)
```

Для большей наглядности подойдёт именованный кортеж — `collections.namedtuple`:

```python
from collections import namedtuple

Pet = namedtuple("Pet", "type name age")
frank = Pet(type="pigeon", name="Френк", age=3)

>>> frank.age
3
```

Это все знают ツ А вот несколько менее известных особенностей:

## Быстрое изменение полей

Что делать, если одно из свойств надо изменить? Френк стареет, а кортеж-то неизменяемый. Чтобы не пересоздавать его целиком, придумали метод `_replace()`:

```python
>>> frank._replace(age=4)
Pet(type='pigeon', name='Френк', age=4)
```

А если хотите сделать всю структуру изменяемой — <code>_asdict()</code>:

```python
>>> frank._asdict()
OrderedDict([('type', 'pigeon'), ('name', 'Френк'), ('age', 3)])
```

## Автоматическая замена названий

Допустим, вы импортируете данные из CSV и превращаете каждую строчку в кортеж. Названия полей взяли из заголовка CSV-файла. Но что-то идёт не так:

```python
# headers = ("name", "age", "with")
>>> Pet = namedtuple("Pet", headers)
ValueError: Type names and field names cannot be a keyword: 'with'

# headers = ("name", "age", "name")
>>> Pet = namedtuple("Pet", headers)
ValueError: Encountered duplicate field name: 'name'
```

Решение — аргумент `rename=True` в конструкторе:

```python
# headers = ("name", "age", "with", "color", "name", "food")
Pet = namedtuple("Pet", headers, rename=True)

>>> Pet._fields
('name', 'age', '_2', 'color', '_4', 'food')
```

«Неудачные» названия переименовались в соответствии с порядковыми номерами.

## Значения по умолчанию

Если у кортежа куча необязательных полей, всё равно приходится каждый раз перечислять их при создании объекта:

```python
Pet = namedtuple("Pet", "type name alt_name")

>>> Pet("pigeon", "Френк")
TypeError: __new__() missing 1 required positional argument: 'alt_name'

>>> Pet("pigeon", "Френк", None)
Pet(type='pigeon', name='Френк', alt_name=None)
```

Чтобы этого избежать, укажите в конструкторе аргумент `defaults`:

```python
Pet = namedtuple("Pet", "type name alt_name", defaults=("нет",))

>>> Pet("pigeon", "Френк")
Pet(type='pigeon', name='Френк', alt_name='нет')
```

`defaults` присваивает умолчательные значения с хвоста. Работает в питоне 3.7+

Для старых версий можно более коряво добиться того же результата через прототип:

```python
Pet = namedtuple("Pet", "type name alt_name")
default_pet = Pet(None, None, "нет")

>>> default_pet._replace(type="pigeon", name="Френк")
Pet(type='pigeon', name='Френк', alt_name='нет')

>>> default_pet._replace(type="fox", name="Клер")
Pet(type='fox', name='Клер', alt_name='нет')
```

Но с `defaults`, конечно, куда приятнее.

## Необычайная лёгкость

Одно из преимуществ именованного кортежа — легковесность. Армия из ста тысяч голубей займёт всего 10 мегабайт:

```python
from collections import namedtuple
import objsize  # 3rd party

Pet = namedtuple("Pet", "type name age")
frank = Pet(type="pigeon", name="Френк", age=None)

pigeons = [frank._replace(age=idx) for idx in range(100000)]

>>> round(objsize.get_deep_size(pigeons)/(1024**2), 2)
10.3
```

Для сравнения, если Pet сделать обычным классом, аналогичный список займёт уже 19 мегабайт.

Так происходит, потому что обычные объекты в питоне таскают с собой увесистый дандер `__dict__`, в котором лежат названия и значения всех атрибутов объекта:

```python
class PetObj:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

frank_obj = PetObj(type="pigeon", name="Френк", age=3)

>>> frank_obj.__dict__
{'type': 'pigeon', 'name': 'Френк', 'age': 3}
```

Объекты-namedtuple же лишены этого словаря, а потому занимают меньше памяти:

```python
frank = Pet(type="pigeon", name="Френк", age=3)

>>> frank.__dict__
AttributeError: 'Pet' object has no attribute '__dict__'

>>> objsize.get_deep_size(frank_obj)
335

>>> objsize.get_deep_size(frank)
239
```

Но как именованному кортежу удалось избавиться от `__dict__`? Читайте дальше ツ

## Богатый внутренний мир

Если вы давно работаете с питоном, то наверняка знаете: легковесный объект можно создать через дандер `__slots__`:

```python
class PetSlots:
    __slots__ = ("type", "name", "age")
  
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

frank_slots = PetSlots(type="pigeon", name="Френк", age=3)
```

У «слотовых» объектов нет словаря с атрибутами, поэтому они занимают мало памяти. «Френк на слотах» такой же лёгкий, как «Френк на кортеже», смотрите:

```python
>>> objsize.get_deep_size(frank)
239

>>> objsize.get_deep_size(frank_slots)
231
```

Если вы решили, что namedtuple тоже использует слоты — это недалеко от истины. Как вы помните, конкретные классы-кортежи объявляются динамически:

```python
Pet = namedtuple("Pet", "type name age")
```

Конструктор namedtuple применяет разную тёмную магию и генерит примерно такой класс (сильно упрощаю):

```python
class Pet(tuple):
    __slots__ = ()
  
    type = property(operator.itemgetter(0))
    name = property(operator.itemgetter(1))
    age = property(operator.itemgetter(2))
  
    def __new__(cls, type, name, age):
        return tuple.__new__(cls, (type, name, age))
```

То есть наш Pet — это обычный `tuple`, к которому гвоздями приколотили три метода-свойства:

- `type` возвращает нулевой элемент кортежа
- `name` — первый элемент кортежа
- `age` — второй элемент кортежа

А `__slots__` нужен только для того, чтобы объекты получились лёгкими. В результате Pet и занимает мало места, и может использоваться как обычный кортеж:

```python
>>> frank.index("Френк")
1

>>> type, _, _ = frank
>>> type
'pigeon'
```

Хитро придумано, а?

## Не уступает дата-классам

Раз уж мы заговорили о генерации кода. В питоне 3.7 появился убер-генератор кода, которому нет равных — дата-классы (dataclasses).

Когда впервые видишь дата-класс, хочется перейти на новую версию языка только ради него:

```python
from dataclasses import dataclass

@dataclass
class PetData:
    type: str
    name: str
    age: int
```

Чудо как хорош! Но есть нюанс — он толстый:

```python
frank_data = PetData(type="pigeon", name="Френк", age=3)

>>> objsize.get_deep_size(frank_data)
335

>>> objsize.get_deep_size(frank)
239
```

Дата-класс генерит обычный питонячий класс, объекты которого изнемогают под тяжестью `__dict__`. Так что если вы начитываете из базы вагон строк и превращаете их в объекты, дата-классы — не лучший выбор.

Но постойте, дата-класс ведь можно «заморозить», как кортеж. Может тогда он станет легче?

```python
@dataclass(frozen=True)
class PetFrozen:
    type: str
    name: str
    age: int

frank_frozen = PetFrozen(type="pigeon", name="Френк", age=3)

>>> objsize.get_deep_size(frank_frozen)
335
```

Увы. Даже замороженный, он остался обычным увесистым объектом со словарём атрибутов. Так что если вам нужны лёгкие неизменяемые объекты (которые к тому же можно использовать как обычные кортежи) — namedtuple по-прежнему лучший выбор.

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Мне очень нравится именованный кортеж:

- честный iterable,
- динамическое объявление типов,
- именованный доступ к атрибутам,
- лёгкий и неизменяемый.

И при этом реализован в 150 строк кода. Что ещё надо для счастья ツ

*Если хотите узнать больше о стандартной библиотеке Python — подписывайтесь на канал [@ohmypy](https://t.me/ohmypy)*

*[33 комментария](https://habr.com/ru/post/438162/#comments)*

