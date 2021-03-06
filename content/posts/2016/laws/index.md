+++
date = 2016-04-12T11:15:02Z
description = "Хороший интерфейс, как робот из рассказов Азимова, подчиняется трем законам."
featured = true
image = "/laws/cover.png"
slug = "laws"
tags = ["interface"]
title = "Законы робототехники в интерфейсе"
subscribe = "dangry"
+++

Интерфейс — это способ, которым человек решает свою задачу:

- войти в квартиру (интерфейс — дверь);
- сообщить машинисту поезда о пожаре (переговорная панель);
- найти на карте аэропорта ближайший туалет (информационный киоск).
- купить цветы в интернет-магазине (форма заказа).

Для человека интерфейс — это внешность и наблюдаемое поведение, а не внутреннее устройство. Пользователь не задумывается о том, как работает механизм или программа изнутри, пока она справляется со своими задачами.

<div class="row">
<div class="col-xs-12 col-sm-10">
    <figure class="image">
        <img class="img-bordered-thin" alt="Яндекс" src="laws-yandex.png">
        <figcaption>Поиск Яндекса — это сложнейшая программа, которая работает на тысячах серверов. Но кого это волнует, когда все знают, что Яндекс — это такая страничка, где быстро можно найти то, что нужно.</figcaption>
    </figure>
</div>
</div>

В проектировании интерфейсов вагон и маленькая тележка правил разной степени универсальности. В то же время, мне нравится выделять три базовых закона, о которых лучше всегда помнить. Из них выводятся все остальные.

Оригинальные законы робототехники придумал писатель-фантаст Айзек Азимов. В рассказах Азимова они защищали людей от произвола машин. А у нас помогут людям не страдать от кривых интерфейсов.

## № 1. Не навредить

Компьютер не может причинить данным человека вред или своим бездействием допустить, чтобы они пострадали.

### Не терять данные пользователя

♞ Человек пять минут вводил реквизиты в квитанцию на оплату, а потом нажал на «Отправить» и получил ошибку:

![Что-то пошло не так](laws-something-gone-wrong.jpg)

Человек нажимает на «повторить попытку», и…

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    Программа открывает пустую форму, пользователь вводит реквизиты заново.
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Программа показывает форму с заполненными реквизитами, ровно как она была до отправки.
</p>
</div>
</div>

### Не перекладывать на человека заботу о сохранности данных

Ленивая программа заставляет человека указывать, когда и что сохранять. Забыл сохранить? Ну, твои проблемы.

♞ Человек дописал статью в текстовом редакторе и решил его закрыть. Реакция программы:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    В документе «Мой документ 132» есть несохранённые изменения. Сохранить их? Да / нет / справка
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    (молча автоматически сохраняет после каждого изменения)
</p>
</div>
</div>

<figure class="image">
    <img class="img-bordered" alt="Автосохранение" src="laws-autosave.png">
    <figcaption>Гуглодокументы моментально сохраняют любые изменения</figcaption>
</figure>

Ленивая программа не несёт ответственности за технические ошибки. Заботливая — страхует от них.

♞ В результате технического сбоя личный дневник в облачном хранилище затёрся версией пятилетней давности. Реакция сервиса:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    Яндекс.Диск: «Извини, дружище. Надеюсь, у тебя есть бэкапы. Лично я прошлые версии не храню».
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Дропбокс: «Хочешь восстановить дневник, как он был до этого досадного происшествия? Нет проблем».
</p>
</div>
</div>

### Помнить привычки человека

Равнодушная программа — как бестолковый сотрудник техподдержки: всегда начинает спрашивать «с чистого листа». Пользователь не барин, может и по второму разу то же самое сделать, и по третьему. Заботливая программа помнит предпочтения человека и старается их учитывать.

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    «Яндекс.Музыка» при старте всегда открывает раздел «подборки». Ей всё равно, что я никогда не слушал эти подборки и не собираюсь.
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Открывать раздел, на котором пользователь остановился в прошлый раз. В моём случае это сохранённые треки. Ещё лучше — включать тот же трек, на котором я прервал прослушивание.
</p>
</div>
</div>

## № 2. Не выносить мозг

Компьютер должен решать задачу пользователя, а не выносить мозг по пустякам. Программа не должна впустую тратить время человека или заставлять его выполнять действия сверх необходимых.

### Не заставлять человека думать

Все, что может делать машина самостоятельно — она должна делать, не вмешивая человека. Помнить промежуточные результаты вычислений, пересчитывать американские размеры одежды в европейские, определять город и индекс, красиво форматировать номер банковской карты.

Для второстепенных задач хорошая программа делает выбор автоматически:

- Вместо того, чтобы заставлять человека придумывать «логин» — использует электронную почту. Даёт войти через соцсети, многим так удобнее.
- Вместо «введите номер телефона в формате 7xxxxxxxxxx» — разрешает свободный ввод и форматирует номер автоматически.
- Вместо того, чтобы с каждой покупкой запрашивать ФИО, адрес и телефон — подставляет их из предыдущего заказа.

<figure class="image">
    <img alt="Вход по эл. почте" src="laws-mif-1.png">
    <figcaption>«<a href="http://www.mann-ivanov-ferber.ru/">Манн, Иванов и Фербер</a>» пускают в личный кабинет по эл. почте без логина и пароля</figcaption>
</figure>

### Решать конечную задачу, а не промежуточную

Хороший робот решает задачу человека, а не ту, что выдумал программист. Если в интернет-магазине покупатель видит «заказ отправлен», этого недостаточно — цель еще не достигнута.

Так лучше:

> Мы приняли заказ. Менеджер перезвонит через полчаса, чтобы согласовать доставку.

Так тоже хорошо:

<blockquote>
    <p>Мы приняли заказ. Сегодня воскресенье, поэтому менеджер перезвонит насчёт доставки завтра с 10 до 11.</p>
    <p>Для тех, кто любит покупать в выходные и праздники, у нас бывают скидки. Подпишитесь <u>на рассылку</u>, чтобы их не пропустить.</p>
</blockquote>

### Не заставлять человека ждать

Компьютер не должен заставлять человека ждать. Ритм взаимодействия устанавливает пользователь.

> Если интернет-магазин десять секунд грузит десяток скриптов веб-аналитики, чата, обратного звонка, виджетов с акциями и черта лысого в сухарях, а я в это время сижу перед экраном и жду, когда увижу карточку товара — то мне такой магазин не нужен.

Программа не имеет права оставить человека в неизвестности:

> Отправил заказ, а она крутит индикатором ожидания, типа «не видишь что ли — работаю». А сама тихо и навсегда сломалась.

Если приказ человека не выполнен, робот обязан немедленно сказать об этом:

> Нет интернета. Мы не успели передать заказ в магазин, но сохранили его на этой странице. Так что когда интернет появится, вы сможете отправить заказ одной кнопкой — заново вводить ничего не придётся.

## № 3. Общаться по-человечески

Плохой интерфейс говорит языком программиста: с удовольствием делится подробностями, как у него всё внутри устроено и что сломалось. Решений он не предлагает — человек умный, сам разберётся. Хороший интерфейс, напротив *по-человечески говорит в чём дело* и помогает справиться с проблемой:

♞ Человек пытается войти в интернет-банк и видит сообщение:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    В целях безопасности подтверждение операции невозможно. Обратитесь в Телефонный центр.
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Кажется, вы сменили SIM-карту. Ответьте на пару вопросов, чтобы получить доступ к интернет-банку: позвоните +7 495 223-23-23 или напишите <u>в чат</u>.
</p>
</div>
</div>

Плохой интерфейс требует, и тем самым бесит человека. Хороший — *объясняет пользу*, и тем самым убеждает:

♞ На форме заказа цветов в интернет-магазине пользователь дошёл до поля «Телефон». Под полем надпись:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    Телефон — обязательное поле
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Курьер позвонит за час до приезда
</p>
</div>
</div>

Плохой интерфейс многословно и путано объясняет. Хороший — *наглядно показывает*.

♞ В CRM-системе появилась новая возможность. Пора рассказать о ней пользователю:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    Система ускоряет заполнение сведений о компании с помощью функций подсказок для реквизитов юридических лиц. Продвинутые возможности полнотекстового поиска делают возможным указание всех сведений за считанные секунды.
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    <img alt="Картинка лучше тысячи слов" src="laws-new-feature.png">
</p>
</div>
</div>

Плохой интерфейс учит человека, как правильно жить. Хороший — *молча делает, но предупреждает* о неприятных последствиях:

<div class="row">
<div class="col-xs-12 col-sm-6">
<p>
    <em>Плохо</em><br>
    Вы задали элемент запрета разрешений. Элементы запрета имеют более высокий приоритет, чем элементы разрешения. Это означает, что пользователь, являющийся членом двух групп, одна из которых имеет разрешение, а другой это разрешение запрещено, не будет иметь это разрешения. Продолжить выполнение операции? Да / нет
</p>
</div>
<div class="col-xs-12 col-sm-6">
<p>
    <em>Лучше</em><br>
    Вы добавили Виктора Васильева в группу «Читатели», и поэтому он не сможет редактировать статьи. Если это не то, чего вы хотели — <u>уберите его из группы</u>.
</p>
</div>
</div>

А ещё хороший интерфейс называет вещи своими именами и не коверкает язык:

- Программа для книжного магазина работает с книгами и открытками, а не «объектами учета».
- В туду-листе осталось «23 задачи», а не «задач: 23»

<p class="align-center">⌘&nbsp;⌘&nbsp;⌘</p>

## Запомнить

Если вы никогда ничего больше не прочитаете о проектировании интерфейсов, но примете и начнёте применять три закона робототехники в своих программах — пользователи будут слать вам лучи благодарности вместо проклятий.

Эти «законы» — просто здравый смысл. То же самое, что вы ожидаете от смышлёного коллеги:

- Не подставлять и не пакостить.
- Работать на совесть и решать проблемы самостоятельно.
- Внятно доносить свою мысль и адекватно общаться.

Следующая статья цикла:

<p class="big">
<a href="/simple-ui">Что делает интерфейс простым</a>
</p>
