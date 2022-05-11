+++
date = 2019-06-29T07:55:19Z
description = "Почему бинарный поиск не всегда быстрый."
image = "/assets/projects/ohmypy-2.png"
slug = "sorted-puzzle"
tags = ["ohmypy"]
title = "Python. Cортировать в конце или держать отсортированным?"
subscribe = "ohmypy"
+++

На днях я предложил подписчикам канала [Oh My Py](http://ohmypy.ru) такую задачку:

<blockquote>
<p>Допустим, вы пишете программу, которой на вход последовательно, одно за другим, приходят числа. Ваша задача — накапливать их как-то, а потом, когда числа перестанут приходить — вернуть отсортированный список.
<p>Как думаете, что будет работать быстрее:</p>
<ul>
  <li>Складывать приходящие числа в неупорядоченную кучу, отсортировать в конце.</li>
  <li>Постоянно поддерживать отсортированный список (с помощью <code>bisect</code>), в конце просто вернуть его.</li>
  <li></li>
</ul>
</blockquote>

Вот результаты голосования:

<div class="row">
<div class="col-xs-12 col-sm-8">
<figure>
  <img class="img-bordered" alt="Результаты голосования" src="sorted-puzzle-poll.png">
  <figcaption>Большинство решило, что быстрее постоянно поддерживать список отсортированным.</figcaption>
</figure>
</div>
</div>

Давайте разберёмся, так ли это.

## Решение

Сразу оговорюсь, что оценивать будем именно чистое время выполнения нашего обработчика. Понятно, что если источник будет присылать по одному числу в минуту, то общее время выполнения будет определяться именно скоростью источника, а не нашим обработчиком — вне зависимости от выбранного алгоритма. Поэтому исходим из того, что источник фигачит числами как из пулемёта.

Мы знаем, что сортировка на *n* числах занимает *O(n logn)* операций. Это сложность варианта «сортировать в конце».

Мы также знаем, что один бинарный поиск занимает *O(log n)* операций. В варианте «поддерживать отсортированным» мы выполняем поиск *n* раз, значит итоговая сложность *O(n logn)*.

Там *O(n logn)* и тут *O(n logn)* — значит, варианты равнозначные, расходимся.

На самом деле нет ツ Посмотрите на реализацию варианта «поддерживать отсортированным»:

```python
def keep_sorted(generator):
    collection = []
    for number in generator:
        index = bisect.bisect(collection, number)
        collection.insert(index, number)
    return collection
```

Да, бинарный поиск выполняется за логарифмическое время. Но после него идёт вставка в массив — она занимает *линейное* время.

Таким образом, на каждое число алгоритм тратит *O(n)* операций, а на *n* чисел — *O(n²)*. Это сильно медленнее, чем *O(n logn)*.

## Проверка

Чтобы не быть голословным, я реализовал оба варианта и сравнил их в действии.

### Подготовка

Сначала подготовим генератор чисел:

```python
import random

# будем генерить числа от 1 до 1 млн
RANGE_SIZE = 1 * 10**6

def number_generator(count):
    for _ in range(count):
        number = random.randint(1, RANGE_SIZE)
        yield number
```

Затем реализуем алгоритм «сортировать в конце»:

```python
from collections import deque

def sort_after(generator):
    collection = deque()
    for number in generator:
        collection.append(number)
    return sorted(collection)
```

И алгоритм «поддерживать отсортированным»:

```python
import bisect

def keep_sorted(generator):
    collection = []
    for number in generator:
        bisect.insort(collection, number)
    return collection
```

### Синхронная работа

Сначала рассмотрим вариант, когда генератор и обработчик работают строго последовательно: генератор присылает число, обработчик складывает его к себе, генератор присылает второе число, обработчик снова складывает, и так далее. Пока обработчик не закончил с числом, генератор не может прислать следующее.

Будем проверять на 1 млн чисел.

```python
count = 1 * 10**6
```

Сортировать в конце:

```python
%%time
sort_after(number_generator(count))
;
```

```
CPU times: user 1.33 s, sys: 20.1 ms, total: 1.35 s
Wall time: 1.35 s
```

Держать отсортированным:

```python
%%time
keep_sorted(number_generator(count))
;
```

```
CPU times: user 1min 25s, sys: 74.9 ms, total: 1min 25s
Wall time: 1min 25s
```

Вариант «сортировать в конце» оказался быстрее в 63 раза (1.35 секунды против 85 секунд).

### Асинхронная работа

Теперь пусть генератор и обработчик работают независимо. Генератор присылает числа с некоторым интервалом, а обработчик независимо складывает их к себе. Генератор не дожидается, пока обработчик закончит с очередным числом — он может прислать новое в любой момент.

Здесь придётся работать в два процесса (отдельно генератор, отдельно обработчик), так что будем использовать очередь для синхронизации. Генератор будет складывать в неё числа, а обработчик — забирать.

Кроме того, добавим генератору задержку:

```python
import random
import time

def number_generator(queue, count, delay):
    for _ in range(count):
        number = random.randint(1, RANGE_SIZE)
        queue.put(number)
        time.sleep(delay)
    queue.put(None)
```

Алгоритмы «сортировать в конце» и «поддерживать отсортированным» не слишком поменяются. Просто теперь они получают числа не из генератора, а из очереди:

```python
from collections import deque

def sort_after(queue):
    collection = deque()
    while True:
        number = queue.get()
        if number is None:
            break
        collection.append(number)
    return sorted(collection)
```

```python
import bisect

def keep_sorted(queue):
    collection = []
    while True:
        number = queue.get()
        if number is None:
            break
        bisect.insort(collection, number)
    return collection
```

Добавим вспомогательную функцию, которая создаёт процессы и запускает тест:

```python
from multiprocessing import Process, Queue

def main(processor, count, delay):
    print(f"count = {count}, delay = {delay}")
    queue = Queue()
    generator = Process(
        target=number_generator,
        args=(queue, count, delay),
        daemon=True,
    )
    consumer = Process(target=processor, args=(queue,), daemon=True)
    
    generator.start()
    consumer.start()
    generator.join()
    consumer.join()
```

Будем проверять на 1 млн чисел и интервале между приходом чисел в 1 микросекунду:

```python
count = 1 * 10**6
delay = 1 * 10**(-6)
```

```python
%%time
main(sort_after, count, delay)
;
```

```
count = 1000000, delay = 1e-06
CPU times: user 3.12 ms, sys: 5.48 ms, total: 8.6 ms
Wall time: 29.3 s
```

```python
%%time
main(keep_sorted, count, delay)
;
```

```
count = 1000000, delay = 1e-06
CPU times: user 3.81 ms, sys: 6.43 ms, total: 10.2 ms
Wall time: 1min 43s
```

Кажется, что разрыв сократился (29 секунд против 103). Но на самом деле эти 29 секунд уходят не на полезную работу, а на «обвязку» — возню вокруг `time.sleep()` и межпроцессное взаимодействие. Чтобы убедиться в этом, сделаем ещё один алгоритм, который вообще не сортирует приходящие числа, а просто возвращает их в финале как есть:

```python
def do_not_sort(queue):
    collection = deque()
    while True:
        number = queue.get()
        if number is None:
            break
        collection.append(number)
    return collection
```

```python
%%time
main(do_not_sort, count, delay)
;
```

```
count = 1000000, delay = 1e-06
CPU times: user 2.93 ms, sys: 5.58 ms, total: 8.52 ms
Wall time: 29.1 s
```

Таким образом, «чистое» время работы «сортировать в конце» по-прежнему составляет около 1 секунды, а «держать отсортированным» — в десятки раз больше.

[Ноутбук](https://gist.github.com/nalgeon/199c30f8a0298c6da9c79559ca848ddc)

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Итого: чистая победа «сортировать в конце» над «держать отсортированным» с большим отрывом.
