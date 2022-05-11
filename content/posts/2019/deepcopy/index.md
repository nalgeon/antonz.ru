+++
date = 2019-06-24T17:02:00Z
description = "С помощью copy.deepcopy()"
image = "/assets/projects/ohmypy-2.png"
slug = "deepcopy"
tags = ["ohmypy"]
title = "Python. Создать полный дубль коллекции"
subscribe = "ohmypy"
+++

У нас ответственная миссия: запустить в космос автомобиль. Сначала подготовим инфраструктуру — собственно машину и мега-пушку:

```python
from dataclasses import dataclass

@dataclass
class Car:
    brand: str
    model: str
    driver: str

class SpaceCannon:
    def launch(self, cars):
        car = cars[0]
        print(f"{car.brand} {car.model} driven by {car.driver} sent to space!")
```

Проверим:

```python
car = Car(brand="Tesla", model="Roadster", driver="Starman")
cars = [car]
cannon = SpaceCannon()
cannon.launch(cars)

Tesla Roadster driven by Starman sent to space!
```

Работает!

Как всякий уважающий себя космический завод, наш умеет копировать машины. Очень удобно — можно сделать копию коллекции машин и всячески над ней издеваться. Например, очистить:

```python
copied_cars = cars[:]
copied_cars.clear()
```

Оригинальный список при этом не пострадал, его можно спокойно запускать:

```python
cannon.launch(cars)
Tesla Roadster driven by Starman sent to space!
```

О, тут инженерам ещё хохма в голову пришла:

```python
copied_cars = cars[:]
copied_cars[0].brand = "ToSky"
copied_cars[0].model = "Zhiguli"
copied_cars[0].driver = "Roskosmos guy"
```

Очень смешно, отправить в космос чела из Роскосмоса на жигулях, ха-ха. Пошутили и хватит, запускаем Теслу:

```python
cannon.launch(cars)
ToSky Zhiguli driven by Roskosmos guy sent to space!
```

Ну вот (((

Проблема в том, что `cars[:]` выполняет так называемое поверхностное копирование — сам список копируется, но в качестве его элементов используются ссылки на элементы оригинального списка.

Поэтому, меняя `copied_cars[0]`, мы превратили оригинальную Теслу в Жигули (что само по себе заслуживает уважения, конечно).

Создать полный дубликат коллекции поможет модуль `copy`:

```python
import copy

car = ...
cars = [car]
copied_cars = copy.deepcopy(cars)
copied_cars[0].model = "Zhiguli"
cannon.launch(cars)

Tesla Roadster driven by Starman sent to space!
```

Во, другое дело.
