+++
date = 2021-12-01T14:50:00Z
title = "Датасет слов английского языка"
description = "Oxford 5000 и другие наборы с произношением."
image = "/words-dataset/cover.png"
slug = "words-dataset"
tags = ["data"]
subscribe = "sqliter"
+++

Обнаружил, что у Оксфордского университета есть списки распространенных слов и выражений английского языка. Доступны в традиционно «удобном» формате — html-амбразуре на сайте либо PDF.

Извлек их и сделал нормальные наборы данных в CSV. Например:

| word | level | pos | definition_url | voice_url |
| ---  | --- | --- | --- | --- |
| abandon | b2 | verb | [📄](https://www.oxfordlearnersdictionaries.com/definition/english/abandon_1) | [🗣️](https://www.oxfordlearnersdictionaries.com/media/english/us_pron_ogg/a/aba/aband/abandon__us_2.ogg) |
| ability | a2 | noun | [📄](https://www.oxfordlearnersdictionaries.com/definition/english/ability_1) | [🗣️](https://www.oxfordlearnersdictionaries.com/media/english/us_pron_ogg/a/abi/abili/ability__us_4.ogg) |
| able | a2 | adjective | [📄](https://www.oxfordlearnersdictionaries.com/definition/english/able_1) | [🗣️](https://www.oxfordlearnersdictionaries.com/media/english/us_pron_ogg/a/abl/able_/able__us_2.ogg) |
| abolish | c1 | verb | [📄](https://www.oxfordlearnersdictionaries.com/definition/english/abolish) | [🗣️](https://www.oxfordlearnersdictionaries.com/media/english/us_pron_ogg/a/abo/aboli/abolish__us_1.ogg) |
| и еще 5000 слов... |

Атрибутика:

-   `word` — слово
-   `pos` — часть речи
-   `level` — уровень (A1, A2, B1, B2, C1)
-   `definition_url` — ссылка на подробное определение
-   `voice_url` — ссылка на озвучку в ogg

<!-- <p class="big">
<a href="https://github.com/nalgeon/words">github.com/nalgeon/words</a>
</p> -->

Посмотреть и скачать:<br>
[**github.com/nalgeon/words**](https://github.com/nalgeon/words)
