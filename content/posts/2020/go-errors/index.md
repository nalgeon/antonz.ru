+++
date = 2020-06-04T14:11:07Z
description = "Ошибки в го особенно уродливы, но это неспроста."
image = "/assets/projects/thankgo.png"
slug = "go-errors"
tags = ["development"]
title = "Красавица и чудовище. Обработка ошибок в Go"
subscribe = "thank_go"
+++

Роб Пайк сказал об ошибках в го:

> Explicit error checking forces the programmer to think about errors — and deal with them — when they arise.

Это правда. Но не вся.

Допустим, я хочу прочитать список целых чисел из текстового файла. Вот как можно сделать это на питоне:

```python
def read_numbers(filename):
    return [int(line.strip()) for line in open(filename)]
```

Или, в более процедурном стиле:

```python
def read_numbers(filename):
    numbers = []
    for line in open(filename):
        num = int(line.strip())
        numbers.append(num)
    return numbers
```

```python
>>> read_numbers("numbers.txt")
[11, 33, 71]
```

Какой прекрасный, лаконичный, понятный код, не правда ли? Сделаем то же самое в го:

```go
func readNumbers(filename string) ([]int, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var numbers []int
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		number, err := strconv.Atoi(scanner.Text())
		if err != nil {
			return nil, err
		}
		numbers = append(numbers, number)
	}

	if err := scanner.Err(); err != nil {
		return nil, err
	}

	if err := file.Close(); err != nil {
		return nil, err
	}

	return numbers, nil
}
```

## Плохо / хорошо

Что плохо в этом коде? (помимо того, что он прямо умоляет разбить на несколько функций вместо одной жирной)

1. Он уродливый.
2. Тяжело понять происходящее, потому что обработка ошибок перемешана с основной логикой.

А вот что хорошо:

1. Видны все ситуации, в которых что-то может пойти не так.
2. Пока пишешь код, го заставляет решить, что делать с каждой ошибкой.

Серьёзный плюс, на самом деле. Необработанные ошибки создают огромное количество багов в программах на других языках. Го же тычет программисту в лицо ошибками и требует явно указать, что с ними делать.

Но всегда ли это плюс? Обычно обработка ошибки происходит не там, где ошибка выброшена, а на более высоком уровне. Часто — на значительно более высоком. В го это приводит к постоянным «пробросам» ошибок наверх:

```go
if err != nil {
    return err
}
```

Такой конструкцией переполнена любая программа на го. Ценность её нулевая, потому что это чисто техническая передача ошибки выше, выше и выше — до момента, когда она будет обработана.

В языках с конструкцией `try-catch` такой костыль не нужен — достаточно поставить `catch` на том уровне, где ошибка будет обработана. При этом на более низких уровнях можно писать код так, как будто никаких ошибок нет — это делает программу проще для понимания и модификации.

На питоне я могу сделать так:

```python
try:
    numbers = read_numbers("numbers.txt")
except Exception as exc:
    print(f"Failed to read numbers: {exc}")
```

И не заботиться внутри `read_numbers()` об обработке ошибок. Если конкретная причина ошибки не важна, это нормальный подход.

Го же вынуждает программиста возиться с каждой ошибкой — даже когда не надо. Роб Пайк сделал выбор за вас, живите с этим.

## Что дальше

Думаю, авторы языка понимали лукавство утверждений о великолепии обработки ошибок в го. Именно этим можно объяснить их предложение добавить в Go 1.14 <a href="https://github.com/golang/go/issues/32437">функцию try</a>.

Вместо:

```go
f, err := os.Open(filename)
if err != nil {
	return ..., err
}
```

Можно было бы писать так:

```go
f := try(os.Open(filename))
```

Сложно представить себе более ужасное решение. Оно несколько повышает читабельность кода, но полностью убивает то единственное, что есть хорошего в работе с ошибками в го — тот самый «explicit error checking», который «forces the programmer to think about errors».

К счастью, волна недоумения от сообщества заставила авторов передумать:

> We still believe that error handling in Go is not perfect and can be meaningfully improved, but it is clear that we as a community need to talk more about what specific aspects of error handling are problems that we should address.

Аминь.

P.S. Результаты голосования:

<div class="row">
<div class="col-xs-12 col-sm-6">
<figure>
  <a href="tg://resolve?domain=thank_go&post=20"><img alt="Что думаете о работе с ошибками в Go?" src="go-errors-poll.png"></a>
  <figcaption>Надо ли всё переписать на PHP 🤔</figcaption>
</figure>
</div>
</div>
