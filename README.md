# Тестовое задание "Адресная книга"

Api на aiohttp.


## Условие задания

**Цель:** Реализовать REST API сервер «Адресная книга»

**Задачи:**
1)   Создать базу данных на РСУБД PostgreSQL согласно структуры ниже.
2)   Написать миграции для автоматического развертывания структуры БД.
3)   Написать скрипт заполняющий данные структуры автоматически
(сгенерировать случайным образом либо заполнить из внешних ресурсов).
4)   Для каждой сущности реализовать полноценный CRUD. 
Для сущности пользователя предусмотреть возможность создания с related сущностями. 
Получение данных реализовать через HTTP POST, создание сущностей HTTP PUT, 
редактирования HTTP PATCH, удаление HTTP DELETE.
5)   В API функциях создания и модификации данных, предусмотреть валидацию по каждому полю сущности. 
Типы валидации определить из контекста поля.
6)   Для методов получения данных предусмотреть возможности сортировки по любому полю.

**Сущности:**
* Пользователи
* Телефоны
* Электронные адреса

**Атрибуты сущностей**:

_Пользователь:_
* ФИО
* Путь к файлу аватара на сервере
* Пол
* Дата рождения
* Адрес проживания (текст)

_Телефоны:_
* ID пользователя
* Вид (Городской/Мобильный)
* Номер телефона

_Электронные адреса:_
* ID пользователя
* Вид (Личная/Рабочая)
* Email


## Как запустить

Понадобится Python третьей версии.

Скачайте код с GitHub. Установите зависимости:

`pip3 install -r requirements.txt`

Заполните файл `config.yaml` следующим образом:

`postgres:
  database: название БД
  user: название пользователя
  password: пароль
  host: localhost
  port: 5432`
  
Создайте таблицы для БД:

`python3 init_db.py`

Заполните таблицы данными:

`python3 fill_db.py`

Запустите проект:

`python3 app.py`

Локально API будет по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) 


## Используемые библиотеки

* [Faker](https://pypi.org/project/Faker/) - для наполнения БД данными.
* [psycopg2](https://pypi.org/project/psycopg2/) - для работы с PostgreSQL.


## Цели проекта

Тестовое задание.