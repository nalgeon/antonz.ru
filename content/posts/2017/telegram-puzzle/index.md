+++
date = 2017-09-06T07:02:05Z
description = "Как помочь Телеграму избавиться от месива каналов, групп и диалогов."
image = "/telegram-puzzle/cover.jpg"
slug = "telegram-puzzle"
tags = ["interface", "puzzle", "telegram"]
title = "Задачка: бардак в телеграме"
+++

<div class="row">
<div class="col-xs-12 col-sm-10">
<p>Я предложил читателям телеграм-канала «<a href="https://t.me/dangry" class="nowrap">интерфейсов без шелухи</a>» такую задачку:</p>
</div>
</div>

<div class="boxed">
<h3>Бардак в Телеграме</h3>
<div class="row">
<div class="col-xs-12 col-sm-8">
<p>Утром вы просматривали любимые каналы, как телеграм вдруг зазвонил. Внезапно, это был Павел Дуров. Не знаю, что на него нашло, но он хочет предложить вам работу. Точнее, разовый проект.</p>
<p>Павел сказал, что гордится идеей каналов в телеграме. «Это как СМИ, только лучше», — сказал он. И продолжал:</p>
<blockquote><p>Когда каналов становится много, работать с ними неудобно. Приходится массово мьютить, но это не спасает — всё равно засоряют список контактов и мешаются с чатами. Больше того, если рабочие чаты ведутся в телеграме — они мешаются с личной перепиской, и всё это превращается в неуправляемое месиво.</p></blockquote>
</div>
<div class="col-xs-12 col-sm-4">
<img alt="Бардак в Телеграме" src="telegram-task.png" style="border: 1px solid #333;">
</div>
</div>
<p>Павел просит вас решить проблему бардака с чатами и каналами в интерфейсе. Дополнительно пожелание: придумать простое и изящное решение, без масштабных переделок. «Не хочу тратить на это много денег», — пояснил он.</p>
<p>Давайте поможем Павлу и сделаем телеграм лучше! Для простоты ограничимся клиентом для мобильных, веб и десктоп не трогаем.</p>
</div>

Спасибо всем, кто прислал свои варианты! Давайте разберём решение. Сразу скажу, что единственно верного варианта тут не вижу. Решения упорядочил по степени вмешательства в интерфейс.

## Большой брат

«Пессимизировать» чаты и каналы, которые пользователь изо дня в день игнорирует. Сначала отключать для них оповещения, затем не поднимать в ленте, несмотря на наличие новых сообщений и, наконец, тихо удалять.

Анализировать активность человека в группах и диалогах в привязке к времени и месту, выявлять рабочую переписку. Глушить рабочие чаты в нерабочее время. В рабочее время глушить каналы.

Не обязательно делать это принудительно. Большой брат может ограничиться советами человеку:

- вот явно рабочие чаты — хочешь глушить их, когда находишься не в офисе и по выходным?
- вот унылые каналы, которые ты не читаешь — хочешь отписаться?
- в этой группе очень много флуда — хочешь заглушить её с 10 до 18?

Сомневаюсь, что Дурову понравилось бы такое решение — так и до Фейсбука с его «умной лентой» недалеко. Но зато отделяет важное от неважного, вообще не трогая интерфейс.

## «Избранное» и «непрочитанное»

<p><em>Избранное</em><br>
Отдельная вкладка или пункт меню. Всё важное в избранное, остальное — в общую кучу. При желании хоть целый день можно провести в избранном, не отвлекаясь на флуд в каналах и группах.</p>

<p><em>Непрочитанное</em><br>
Отдельная вкладка или пункт меню. Спасает от проблемы «потеряшек», когда чат с непрочитанными сообщениями сполз далеко вниз из-за обилия более новых, но прочитанных.</p>

Оба решения простые, отлично сочетаются друг с другом и прочими вариантами.

## Диалоги, группы и каналы

Сделать отдельные вкладки для каждой сущности: диалоги, группы, каналы, боты. Это уже реализовано в альтернативном клиенте Plus Messenger и неплохо работает:

<div class="row">
<div class="col-xs-12 col-sm-6 col-md-5">
<p><img alt="Диалоги, группы и каналы" src="telegram-tabs.png" class="bordered"></p>
</div>
<div class="col-xs-12 col-sm-6">
<p>Plus Messenger зачем-то разделяет группы и супергруппы (хотя это чисто техническое деление), но в остальном устроен весьма разумно. Количество непрочитанных показывает отдельно по каждой вкладке.</p>
<p>Заодно использует отдельные вкладки «избранное» и «непрочитанное».</p>
</div>
</div>

## Личные и рабочие

Разновидность «избранного»: отделяем не важное от второстепенного, а рабочее от личного. Соня Яковчук нарисовала скетч для айфона:

<div class="row">
<div class="col-xs-12 col-sm-6 col-md-5">
<p><img alt="Личные и рабочие" src="telegram-personal-working.jpg"></p>
</div>
<div class="col-xs-12 col-sm-6">
<p>Как видите, разделение на личные и рабочие прекрасно сочетается с делением на чаты и каналы.</p>
<p>А Никита Лаптев предложил вместо переключения по вкладкам сделать отдельные экраны и переходить туда-сюда свайпами влево-вправо.</p>
<p>При переключении на «личные» можно автоматически отключать оповещения от «рабочих», и наоборот. Или оставить это на усмотрение человека — главное, чтобы можно было заглушить раздел целиком.</p>
</div>
</div>

## Категории или теги

Отмечать чаты произвольными тегами: друзья, родственники, работа, секретный проект, новости, интерфейсы, всё что душе угодно. А дальше переключаться между ними или мьютить прямо группами.

<div class="row">
<div class="col-xs-12 col-sm-6 col-md-5">
<p><img alt="Категории или теги" src="telegram-tags.png"></p>
</div>
<div class="col-xs-12 col-sm-6">
<p>Это Slack, но возьмите любой почтовый клиент или RSS-ридер, и увидите такую же логику: папки, категории, теги.</p>
<p>Самый популярный вариант — его предложили 40% участников.</p>
</div>
</div>

## Приятные мелочи

Читатели прислали несколько механик, которые хоть и не относятся напрямую к задаче, пригодились бы в телеграме:

> _Денис Токарев_
> Отмечать чат прочитанным по свайпу вправо.

Удобно, если я просто хочу убрать кучу непрочитанных с глаз долой, не заходя в переписку.

> _Анонимус_
> Каналы должны быть по умолчанию замьючены

Полностью поддерживаю. Добросовестные авторы каналов и так публикуют в режиме Silent Broadcast, а недобросовестных надо к этому принуждать. Больше того, я бы и группы по умолчанию глушил (у меня все группы вручную замьючены — ни разу об этом не пожалел).

> _Анонимус_
> Это мессенджер, и главное — переписка, люди, общение. Поэтому: собеседники всегда в топе, а каналы и чаты — всегда ниже переписок с людьми.

Согласен, если речь идёт только о непрочитанных. Я бы даже более строгий порядок ввёл: диалоги > группы > каналы.

<p class="text-centered">⌘ ⌘ ⌘</p>

Было ещё несколько решений, но там такие космолёты, что я не готов всерьёз их обсуждать.

Ещё раз спасибо всем участникам! Мы продолжим ツ

<div class="row">
<div class="col-xs-12 col-sm-10 col-md-8"><p><em>Решайте задачки на канале <span class="nowrap"><i class="fa fa-star-o color-sin"></i> «<a href="https://t.me/dangry">Интерфейсы без шелухи</a>»</span></em></p></div>
</div>
