+++
date = 2022-05-02T13:00:00Z
title = "Постраничный итератор в Python"
description = "Обходим датасет страницами для быстрой пакетной обработки."
image = "/page-iterator/cover.png"
slug = "page-iterator"
tags = ["development", "ohmypy"]
featured = true
subscribe = "ohmypy"
+++

Предположим, вы считаете статистику по огромному датасету игрушек, проданных по всей стране за прошлый год:

```python
reader = fetch_toys()
for item in reader:
    process_single(item)
```

`process_single()` занимает 10 мс, так что 400 млн игрушек обработаются за 46 дней 😱

В результате оживленного диалога вам удается убедить разработчиков, что так не очень быстро. На свет появляется функция `process_batch()`, которая обрабатывает 10000 игрушек за 1 сек. Это уже 11 часов на все игрушки, что значительно приятнее.

Как бы теперь пройти по датасету пакетами по 10 тысяч записей? Тут и пригодится постраничный итератор!

## Наивный постраничник

Пройдем по исходной последовательности, постепенно заполняя страницу. Как заполнится — отдадим через `yield` и начнем заполнять следующую. Будем продолжать, пока исходная последовательность не закончится:

```python
def paginate(iterable, page_size):
    page = []
    for item in iterable:
        page.append(item)
        if len(page) == page_size:
            yield page
            page = []
    yield page
```

```python
reader = fetch_toys()
page_size = 10_000
for page in paginate(reader, page_size):
    process_batch(page)
```

Реализация рабочая, но есть проблемка. Такой постраничный обход заметно медленнее обычного итерирования по одной записи.

## Скорость обхода

Сравним два обхода — одиночный и постраничный:

```python
def one_by_one(a, b):
    """Processes records one-by-one, without pagination"""
    rdr = reader(a, b)
    for record in rdr:
        process_single(record)

def batch(page_size, a, b):
    """Processes records in batches, with pagination"""
    rdr = reader(a, b)
    for page in paginate(rdr, page_size):
        process_batch(page)

times = 10

page_size = 10_000
a = 1_000_000
b = 2_000_000

fn = lambda: one_by_one(a, b)
total = timeit.timeit(fn, number=times)
it_time = round(total * 1000 / times)
print(f"One-by-one (baseline): {it_time} ms")

fn = lambda: batch(page_size, a, b)
total = timeit.timeit(fn, number=times)
it_time = round(total * 1000 / times)
print(f"Fill page with append(): {it_time} ms")
```

Вот результат на 1 млн записей и странице размером в 10 тысяч:

```
One-by-one (baseline):   161 ms
Fill page with append(): 227 ms
```

Постраничный обход медленнее почти в полтора раза!

Дело в том, что на каждой итерации цикла мы создаем новый пустой список и затем постепенно заполняем его. Питону приходится постоянно увеличивать размер массива под списком, а это затратная операция — O(n) от количества элементов в списке.

## Фиксированная страница

Попробуем заранее создать список нужной длины и использовать его для всех страниц.

```python
def paginate(iterable, page_size):
    page = [None] * page_size
    idx = 0
    for item in iterable:
        page[idx] = item
        idx += 1
        if idx == page_size:
            yield page
            idx = 0
    yield page[:idx]
```

Повторим сравнение:

```
One-by-one (baseline):   161 ms
Fill page with append(): 227 ms
Use fixed-size page:     162 ms
```

Заметно быстрее! Скорость сравнялась с обычным итерированим по одной записи.

## Итерация срезами

Можно ли ещё быстрее? Алгоритмически — нет. А вот практически — да, если перенести как можно больше действий из кода на питоне в библиотечный код на си. В этом поможет модуль `itertools()` и его функция `islice()`:

```python
def paginate(iterable, page_size):
    it = iter(iterable)
    slicer = lambda: list(itertools.islice(it, page_size))
    return iter(slicer, [])
```

Вот что здесь происходит:

-   `islice()` создаёт итератор (назовем его слайсером), который обходит переданную ему последовательность, пока не выберет из нее `page_size` элементов;
-   `list()` выбирает все элементы из этого маленького итератора — получается страница;
-   поскольку `islice()` работает поверх основного итератора, при следующем вызове он продолжит с того же места, где остановился до этого;
-   конструкция `iter(slicer, [])` создает итератор, который на каждом шаге вызывает слайсер;
-   таким образом, функция `paginate()` возвращает итератор, который на каждом шаге выбирает очередную страницу через слайсер, провигаясь по основной последовательности — пока она не закончится.

Посмотрите, до чего хорош такой вариант:

```
One-by-one (baseline):   161 ms
Fill page with append(): 227 ms
Use fixed-size page:     162 ms
Use islice:               93 ms
```

На 40% быстрее обычного итератора по одной записи!

## Итого

Постраничный обход отлично работает везде, где пакетная операция выполняется сильно быстрее набора одиночных. Чтобы не писать такой обход каждый раз с нуля, удобно использовать универсальный _постраничный итератор_.

Постраничный итератор, который динамически заполняет список, работает медленно — из-за постоянного изменения размера массива. Лучше использовать список фиксированного размера, а еще лучше — итерацию на основе `itertools.islice()`

Рекомендую!

[песочница](https://replit.com/@antonz/page-iterator#main.py)
