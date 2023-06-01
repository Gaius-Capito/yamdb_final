# YaMDb API

![example workflow](https://github.com/Gaius-Capito/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения. Сами произведения 
в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.

Взаимодействие с БД осуществляется через Api.

Стек:
- Django 3.2
- DRF 3.12.4
- djangorestframework-simplejwt 4.7.2
- PyJWT 2.1.0

Список запросов и эндпоинтов описан в документации ReDoc, доступной по адресу:
```
http://localhost/redoc/
```



## Развертывание в Docker:
Клонировать репозиторий и перейти в него в командной строке: 

``` 
https://github.com/Gaius-Capito/infra_sp2.git 
```
Переходим в директорию с фалом docker-compose.yaml

Команда для сборки контейнеров:
```
docker-compose up -d --build
```
Выполняем миграции
```
docker-compose exec web python manage.py migrate
```
Создаем суперппользователя
```
docker-compose exec web python manage.py createsuperuser
```
Собираем статику
```
docker-compose exec web python manage.py collectstatic --no-input
```

### Заполните .env файл своими данными:
Расположение файла: /infra_sp2/infra/.env
```
# указываем, с какой БД работаем
DB_ENGINE=django.db.backends.postgresql
# имя базы данных
DB_NAME=
# логин для подключения к базе данных
POSTGRES_USER=
# пароль для подключения к БД (установите свой)
POSTGRES_PASSWORD=
# название сервиса (контейнера)
DB_HOST=
# порт для подключения к БД
DB_PORT=
```

Авторы: 
```
https://github.com/maxwellhousee - Максим Нуриев
```
```
https://github.com/Sheleg0v - Иван Шелегов
```
```
https://github.com/Gaius-Capito - Владислав Бунин
```

http://51.250.12.162/