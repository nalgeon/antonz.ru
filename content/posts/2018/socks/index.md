+++
date = 2018-04-16T16:06:54Z
description = "Чтобы не зависеть от тормозных публичных проксей."
image = "/socks/cover.jpg"
slug = "socks"
tags = ["life", "telegram"]
title = "Как сделать собственный прокси для Телеграма"
+++

В России окончательно заблокировали Телеграм. Чтобы он продолжил работать, нужен либо VPN (сложный путь) либо SOCKS5-прокси (простой путь). Я выбираю простой. Есть готовые прокси, но если вы хотите поднять собственный — вот как это сделать.

Прежде всего, потребуется виртуальный сервер. Я лично предпочитаю [Digital Ocean](https://m.do.co/c/b862c8d73641) (реферальная ссылка, по которой бесплатно дают $10 — хватит на 2 месяца). Но можно попробовать другие облака, у которых есть бесплатные микро-сервера:

- [Amazon EC2](https://aws.amazon.com/ru/ec2/)
- [Google Cloud Platform](https://cloud.google.com/compute/pricing)
- [Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/app-service/)

В качестве операционной системы я выбрал Ubuntu 16.04. Рекомендую отключить вход под рутом и настроить сертификат — вот [инструкция](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-16-04).

Когда виртуальный сервер готов, заходим на него по SSH и устанавливаем SOCKS5-сервер Dante:

```
sudo apt update
sudo apt install -y dante-server
```

В убунте ставится древняя версия Данте — 1.1.19. Но её вполне достаточно.

Настраиваем Данте в файле `/etc/danted.conf`. Редактировать проще всего программой `nano`:

    sudo nano /etc/danted.conf

Удаляем содержимое и вставляем свой конфиг:

```
logoutput: stderr
internal: eth0 port = 1080
external: eth0

method: username
user.privileged: root
user.notprivileged: nobody
user.libwrap: nobody

client pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: error
}

pass {
    from: 0.0.0.0/0 to: 0.0.0.0/0
    log: error
}
```

Выходим из редактора с сохранением: `Ctrl+O`, затем `Enter`, затем `Ctrl+X`

Создаём пользователя, который будет подключаться через прокси, и устанавливаем ему пароль:

```
sudo useradd --shell /usr/sbin/nologin telegram
sudo passwd telegram
```

Запускаем Данте:

    sudo systemctl restart danted

Готовим ссылку для автоматической настройки телеграма:

    tg://socks?server=IP_АДРЕС&port=1080&user=telegram&pass=ПАРОЛЬ

Вместо «IP_АДРЕС» подставьте IP-адрес сервера, а вместо «ПАРОЛЬ» — пароль пользователя, которого создали чуть раньше.

Скидываем ссылку в личный чат в телеграме (Saved Messages), тыкаем на неё и соглашаемся применить настройки. Всё, телеграм работает через прокси.

