# api_final
### Описание:
В данном проекте реализован программный интерфейс "REST API" блога. 
Авторизованным клиентам пользователей доступно создание, редактирование,
комментирование постов. Также имеется возможность подписываться на 
авторов и публиковать посты в группах

### Установка:
* Клонировать репозиторий
* Установить и активировать виртуальное окружение
```
python3 -m venv venv
source venv/bin/activate
```
* Установить зависимости проекта
```
pip install -r requirements.txt
```
* Выполнить миграции
```
python3 yatube_api/manage.py makemigrations
```
* Запустить сервер
```
python3 yatube_api/manage.py runserver
```

Примеры:
api final
fdgrd

### Примеры:
Получение списка публикаций
````
GET     /api/v1/posts/

{
    "count": 123,
    "next": "http://api.example.org/accounts/?offset=400&limit=100",
    "previous": "http://api.example.org/accounts/?offset=200&limit=100",
        "results": [
        {
            "id": 0,
            "author": "string",
            "text": "string",
            "pub_date": "2021-10-14T20:41:29.648Z",
            "image": "string",
            "group": 0
        }
    ]
}
````
Получение одной публикации
````
GET /api/v1/posts/{id}
{
    "id": 0,
    "author": "string",
    "text": "string",
    "pub_date": "2019-08-24T14:15:22Z",
    "image": "string",
    "group": 0
}
````
Добавление комментария к посту
````
POST api/v1/posts/{post_id}/comments/
{
    "text": "string"
}

Response sample
{
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
}
````
