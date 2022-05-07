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

```javascript
function speak(text) {
    const message = new SpeechSynthesisUtterance();
    message.lang = "ru-RU";
    // голос женский
    message.voice = getVoice("Milena");
    // или мужской
    // message.voice = getVoice("Yuri");
    message.text = text;
    // тембр и скорость по вкусу
    message.pitch = 0.8;
    message.rate = 0.9;
    window.speechSynthesis.speak(message);
}
```

<p>
    <a class="button" href="https://codepen.io/nalgeon/pen/LBJNXG/?editors=1010" target="_blank">
        песочница
    </a>
</p>

Функция `speak` создаёт говорилку и озвучивает переданный текст на русском языке.

### Распознавание речи

Работает только в хроме и фаерфоксе, причём у каждого по-своему. На андроиде тоже работает, хотя функциональность ограничена по сравнению с десктопом. Реализуется посложнее, но тоже терпимо — 40 строчек джаваскрипта:

```javascript
class Recognizer {
    constructor() {
        this.recognition = new SpeechRecognition();
        this.recognition.lang = "ru-RU";
        this.isRecognizing = false;
        this.transcript = "";
    }

    start(handler) {
        this.transcript = "";
        this.recognition.onresult = (event) => {
            this.onResult(event, handler);
        };
        this.recognition.start();
        this.isRecognizing = true;
    }

    stop() {
        this.recognition.abort();
        this.isRecognizing = false;
    }

    onResult(event, handler) {
        var interim_transcript = "";
        for (var i = event.resultIndex; i < event.results.length; ++i) {
            var result = event.results[i];
            if (result.isFinal) {
                this.transcript += result[0].transcript;
            } else {
                interim_transcript += result[0].transcript;
            }
        }
        handler(interim_transcript);
    }
}
```

<p>
    <a class="button" href="https://codepen.io/nalgeon/pen/XBPKrW/?editors=1010" target="_blank">
        песочница
    </a>
</p>

Распознавалка — в классе `Recognizer`. Начинает слушать после вызова `start()`, заканчивает после `stop()`. Накапливает распознанный текст в свойстве `transcript`. Умеет возвращать промежуточные результаты распознавания, если передать обработчик в `start()`:

```javascript
recognizer.start((text) => {
    txtInterim.value = text;
    txtMessage.value = recognizer.transcript;
});
```

Добрый человек Tal Ater сделал удобную обёртку над API распознавания — библиотеку [annyang](https://github.com/TalAter/annyang). С ней всё ещё проще.

_И подписывайтесь на <a href="https://twitter.com/nalgeon">**@nalgeon**</a> в твитере, чтобы не пропустить новые заметки 🚀_
