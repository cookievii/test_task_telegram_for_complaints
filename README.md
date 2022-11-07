# Тестовое задание: Бот для приема жалоб и предложений ✉.

----------

### Стэк технологий:

* python = 3.11
* aiogram = 2.22.2
* python-dotenv = 0.21.0
* sqlalchemy = 1.4.42
* black = 22.10.0
* isort = 5.10.1

----------

### Описание проекта

_*Бот для приема жалоб и предложений - взаимодействует дополнительно с 3-мя группами ("Администраторы", "Жалобы", "
Предложения".) с предварительной регистрацией пользователей.*_

- _Группа "Администраторы" может заблокировать/разблокировать пользователя, отправлять рассылку все пользователям,
  смотреть полную информацию о пользователе по любому аргументу._


- Реализована возможность оставлять жалобы (Форма заполнения жалобы: Адрес, Фото, Описание). Новые жалобы отправляются в
  группу "Жалобы".


- Реализована возможность оставлять предложения по улучшению (Форма заполнения предложения: Описание). Новые предложения
  отправляются в группу "Предложения".


- Реализована возможность оставлять заявку на обратную связь. Новые заявки отправляются в группу "Администраторы".


- Реализована возможность оставлять сообщения в группу "Администраторы". Сообщения отправляются в группу "
  Администраторы" (Администратор может сразу ответить на сообщения).


- Реализована возможность регистрации по форме ("Имя", "Номер телефона").


- Реализована возможность менять "Имя" и "Номер телефона" после регистрации.

----------

### Установка:

```bash
# - Cкачайте:
git clone git@github.com:cookievii/telegram_bot_for_complaints.git

# - Перейдите в папку telegram_bot_for_complaints репозитория с помощью команды ;
cd telegram_bot_for_complaints/

# - Создаем файл .env -файла(Шаблон наполнения показан ниже).
touch .env

# - Запустите бота в контейнере:
docker-compose up -d
```

### Шаблон наполнения .env -файла:

```bash
TOKEN_TELEGRAM=**********************************************  # Телеграм токен для подключения к боту.
DATEBASE_NAME=datebase.sqlite

# ID дополнительных групп
COMPLAINT_GROUP=**********  # ID чата группы "Жалобы"  для получения сообщений от бота.
OFFERS_GROUP=**********  # ID чата группы "Предложения" для получения сообщений от бота.
ADMIN_GROUP=**********  # ID чата группы "Администраторы" для получения сообщений от бота.
```

### Авторы:

* **Валитов Ильмир Илсурович**
  GitHub - [cookievii](https://github.com/cookievii)

----------

### MIT License:

Copyright (c) 2022 [cookievii](https://github.com/cookievii)

----------
