+++
date = 2018-08-07T12:29:34Z
description = "Местами даже неплохо работает."
image = "/speech-api/cover.png"
slug = "speech-api"
tags = ["development"]
title = "Синтез и распознавание речи в 50 строк на JavaScript"
+++

Если вы, как большинство нормальных людей, не следите пристально за развитием веб-API, то вот краткая сводка их успехов в обработке речи.

### Синтез речи

Вовсю работает в нормальных браузерах. Реализуется в несколько строчек на джаваскрипте:

<p data-height="265" data-theme-id="0" data-slug-hash="LBJNXG" data-default-tab="js,result" data-user="nalgeon" data-pen-title="Синтез речи" class="codepen">See the Pen <a href="https://codepen.io/nalgeon/pen/LBJNXG/">Синтез речи</a> by Anton (<a href="https://codepen.io/nalgeon">@nalgeon</a>) on <a href="https://codepen.io">CodePen</a>.</p>

<br>

Функция speak создаёт говорилку и озвучивает переданный текст на русском языке.

### Распознавание речи

Работает только в хроме и фаерфоксе, причём у каждого по-своему. На андроиде тоже работает, хотя функциональность ограничена по сравнению с десктопом. Реализуется посложнее, но тоже терпимо — 40 строчек джаваскрипта:

<p data-height="400" data-theme-id="0" data-slug-hash="XBPKrW" data-default-tab="js,result" data-user="nalgeon" data-pen-title="Распознавание речи" class="codepen">See the Pen <a href="https://codepen.io/nalgeon/pen/XBPKrW/">Распознавание речи</a> by Anton (<a href="https://codepen.io/nalgeon">@nalgeon</a>) on <a href="https://codepen.io">CodePen</a>.</p>

<br>

Распознавалка — в классе Recognizer. Начинает слушать после вызова `start()`, заканчивает после `stop()`. Накапливает распознанный текст в свойстве `transcript`. Умеет возвращать промежуточные результаты распознавания, если передать обработчик в `start()`:

```javascript
recognizer.start((text) => {
  txtInterim.value = text;
  txtMessage.value = recognizer.transcript;
});
```

Добрый человек Tal Ater сделал удобную обёртку над API распознавания — библиотеку [annyang](https://github.com/TalAter/annyang). С ней всё ещё проще.

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>И подписывайтесь на <span class="nowrap"><i class="fas fa-kiwi-bird"></i> «<a href="tg://resolve?domain=ohmypy">Oh My Py</a>»</span>, это лучше любого JavaScript</em></p></div>
</div>

<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

