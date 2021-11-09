+++
date = 2020-05-05T15:16:48Z
description = "Через мейкфайлы (да, они хороши)."
image = "/makefile/cover.png"
slug = "makefile"
tags = ["development", "ohmypy"]
title = "Автоматизация задач в Python-проекте"
+++

Когда разрабатываешь библиотеку или приложение, всегда найдутся задачи, которые выполняешь изо дня в день:

- проверить код линтерами,
- прогнать тесты с замером покрытия,
- запустить в докере,
- ...

JS-разработчикам повезло (ха): у них в `package.json` есть специальная секция `scripts` для таких штук:

```
{
    ...
    "scripts": {
        "format": "prettier --write \"src/**/*.ts\"",
        "lint": "tslint -p tsconfig.json",
        "test": "jest --coverage --config jestconfig.json",
    },
    ...
}
```

Для Питона ничего подобного не предусмотрено. Можно, конечно, сделать по sh-скрипту на каждую задачу, но это замусоривает каталог проекта, да и хотелось бы все такие задачи держать вместе. А ставить отдельный таск-раннер или использовать встроенный в IDE совсем уж странно.

Хорошая новость: на линуксе и макоси уже есть отличное средство автоматизации задач для любых проектов — мейкфайлы (`Makefile`).

## Makefile для любых задач

Возможно, вы, как и я, думали, что мейкфайлы — странная штука из 70-х годов прошлого века, которая нужна для сборки кода на `C`. Всё так ツ Но они прекрасно подходят для автоматизации вообще любых задач.

Вот как это может выглядеть в питонячем проекте. Создаём файл с названием `Makefile`:

```
coverage:  ## Run tests with coverage
	coverage erase
	coverage run --include=dadata/* -m pytest -ra
	coverage report -m

deps:  ## Install dependencies
	pip install black coverage flake8 mypy pylint pytest tox

lint:  ## Lint and static-check
	flake8 dadata
	pylint dadata
	mypy dadata

push:  ## Push code with tags
	git push && git push --tags

test:  ## Run tests
	pytest -ra
```

И запускаем, например, линтер с тестами:

```
$ make lint coverage

flake8 dadata
pylint dadata
...
mypy dadata
...
coverage erase
coverage run —include=dadata/* -m pytest -ra
...
coverage report -m
Name Stmts Miss Cover Missing
--------------------------------------------------
dadata/__init__.py 3 0 100%
dadata/client.py 56 0 100%
--------------------------------------------------
TOTAL 59 0 100%
```

## Возможности

### Цепочки действий

Задача может включать несколько действий, как `lint` в примере выше:

```
lint:
	flake8 dadata
	pylint dadata
	mypy dadata
```

Каждое действие выполняется в отдельном подпроцессе, так что если нужно выполнить связанную цепочку действий (например, `cd` и `git pull`) — объединяем их через `&&`:

```
schemas:
	cd iuliia/schemas && git pull && cd ../..
```

### Зависимости между задачами

Допустим, задача `test` должна обязательно сначала выполнять линтинг, а потом уже запускать тесты. Указываем `lint` как зависимость для `test`, и готово:

```
test: lint
	pytest -ra
```

Можно указать несколько зависимостей — через пробел.

Либо задачи могут явно вызывать друг друга:

```
lint:
	flake8 dadata
	pylint dadata
	mypy dadata

test:
	pytest -ra

prepare:
	make lint
	make test
```

### Параметры задач

Допустим, задача `serve` запускает статический сайт, а IP и порт хочется сделать настройкой. Нет проблем:

```
serve:
	python -m http.server dist --bind $(bind) $(port)
```

Запускаем с параметрами:

```bash
$ make serve bind=localhost port=3000
```

Можно указать значения по умолчанию:

```
bind ?= localhost
port ?= 3000
serve:
	python -m http.server dist --bind $(bind) $(port)
```

Теперь при вызове `make` указывать их не обязательно:

```bash
$ make serve bind=192.168.0.1
$ make serve port=8000
$ make serve
```


### И ещё много чего

Если описанных возможностей недостаточно, смотрите замечательные руководства:

- [Learn Makefiles with the tastiest examples](https://makefiletutorial.com)
- [Automation and Make](https://swcarpentry.github.io/make-novice/reference.html).

## В дикой природе

Пара примеров мейкфайлов из моих проектов:

- [dadata](https://github.com/nalgeon/dadata-py/blob/master/Makefile)
- [iuliia](https://github.com/nalgeon/iuliia-py/blob/master/Makefile)

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

Мейкфайлы отлично подходят для автоматизации рутинных задач вне зависимости от языка, на котором вы пишете. Используйте их!

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>И подписывайтесь на <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="https://t.me/ohmypy">Oh My Py</a>»</span></em></p></div>
</div>



