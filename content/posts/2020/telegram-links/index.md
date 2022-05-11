+++
date = 2020-05-15T11:17:43Z
description = "Без рекламы и Росогорода."
image = "/telegram-links/cover.png"
slug = "telegram-links"
tags = ["telegram"]
title = "Ссылки на телеграм в вебе"
+++

*Телеграм разблокировали в июне 2020 года, так что теперь можно ставить обычные ссылки и не заморачиваться. Но если что — вы знаете, что делать.*

В рунете заблокирован домен t.me, через который работают ссылки на телеграм. Сервисы-заменители (t-do.ru и прочие) напичканы рекламой и в любой момент могут перестать работать. Используйте лучше нативные ссылки — они гарантированно работают на любом устройстве, где установлен телеграм. И никакой Роскомнадзор ничего с этим не сделает.

Вот как это работает:

## Канал

```
https://t.me/название
→ tg://resolve?domain=название
```

пример: [интерфейсы без шелухи](tg://resolve?domain=dangry)

## Заметка в канале

```
https://t.me/название/номер
→ tg://resolve?domain=название&post=номер
```

пример: [всё о транслитерации](tg://resolve?domain=dangry&post=256)

## Группа по приглашениям

```
https://t.me/joinchat/идентификатор
→ tg://join?invite=идентификатор
```

пример: [датавиз-чат](tg://join?invite=CxZg5goGc6rlWGjcvOYrpA)

## Стикер-пак

```
https://t.me/addstickers/название
→ tg://addstickers?set=название
```

пример: [Гарольд скрывает боль](tg://addstickers?set=HideThePainHarold)

## Поделиться ссылкой в телеграме

```
https://t.me/share/url?url=ссылка&text=описание
→ tg://msg_url?url=ссылка&text=описание
```

пример: [antonz.ru](tg://msg_url?url=antonz.ru&text=Отличный+блог+о+разработке+продуктов)

## Нюансы

Если телеграм на устройстве не установлен, то ссылки не откроются. Но если вы ставите ссылки на телеграм, а у читателя его нет — скорее всего, он не ваша целевая аудитория. Так что невелика потеря.
    
Нативные ссылки не работают в соцсетях (твитер, фейсбук), так что в них придётся использовать t.me.

## Генератор нативных ссылок из обычных

Введите «обычную» ссылку (с t.me) и получите «нативную», которая открывается вне зависимости от блокировок Телеграма:

<style>
#source {
  display: block;
  width: 100%;
  padding: 0.25rem 0.5rem;
  font-size: 1rem;
}
</style>

<div class="row">
<div class="col-xs-12 col-sm-8">
    <div style="margin-bottom: 0.8em;">
        <input id="source" placeholder="https://t.me/...">
    </div>
    <div>
        Нативная ссылка: <a id="native" href="#"></a>
    </div>
</div>
</div>

<script>
var txtSource = document.getElementById("source");
var lnkNative = document.getElementById("native");
txtSource.addEventListener("change", onSourceChange);

var re = /(?:(?:https?:\/\/)?t(?:elegram)?\.me\/)?(.+)/;

function onSourceChange(event) {
  var source = event.target.value;
  var target = telefy(source);
  lnkNative.innerHTML = target;
  lnkNative.setAttribute("href", target);
}

function telefy(source) {
  var matches = re.exec(source);
  if (matches.length < 2) {
    return "";
  }
  var parts = matches[1].split("/");
  var target = "";
  switch (parts[0]) {
    case "joinchat":
      target = joinchat(parts[1]);
      break;
    case "addstickers":
      target = addstickers(parts[1]);
      break;
    case "share":
      target = share(parts[1]);
      break;
    default:
      target = resolve(parts[0], parts[1]);
  }
  return "tg://" + target;
}

function resolve(name, post) {
  if (post) {
    return "resolve?domain=" + name + "&post=" + post;
  }
  return "resolve?domain=" + name;
}

function joinchat(name) {
  return "join?invite=" + name;
}

function addstickers(name) {
  return "addstickers?set=" + name;
}

function share(qs) {
  qs = qs.split("?")[1];
  return "msg_url?" + qs;
}
</script>

<br>
    
<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>
    
Идеального способа ставить ссылки на телеграм в России не существует:
    
- ссылки через t.me не откроются без VPN,
- ссылки через прокси-сайты ненадёжны,
- нативные ссылки не работают в соцсетях.

Но пока Росогород блокирует телеграм — я за нативные ссылки везде, где это работает.
