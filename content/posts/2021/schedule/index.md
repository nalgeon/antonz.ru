+++
date = 2021-05-22T08:31:00Z
description = "С помощью schedule."
image = "/assets/projects/ohmypy-2.png"
slug = "schedule"
tags = ["package", "ohmypy"]
title = "Планировщик задач на Python"
subscribe = "ohmypy"
+++

В стандартной библотеке есть встроенный планировщик задач (а чего вообще в ней нет?). Подробно расскажу в другой раз, но в целом он, скажем так, не слишком юзер-френдли.

Поэтому Дэн Бэйдер сделал [**schedule**](https://github.com/dbader/schedule/) — «планировщик для людей». Смотрите, какой милый:

```python
import schedule
import time

def job():
  print("I'm working...")

schedule.every().hour.do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().day.at("10:30").do(job)

while True:
  schedule.run_pending()
  time.sleep(1)
```

Ноль зависимостей, чистый и великолепно документированный код, примеры на все случаи жизни.
