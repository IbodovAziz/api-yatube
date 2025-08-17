# Yatube API (DRF + Token Auth)

API для проекта Yatube: работа с постами, группами и комментариями.  
API доступен только аутентифицированным пользователям (аутентификация — токенами).  
Автор может изменять/удалять только свой контент; попытка правки чужого — `403 Forbidden`.  
Неавторизованные запросы получают `401 Unauthorized`.

## Стек
- Python 3.10+
- Django 3.2+/4.x
- Django REST framework
- djangorestframework-authtoken

## Быстрый старт (локально)
```bash
# 1) Установить зависимости
pip install -r requirements.txt

# 2) Применить миграции
python manage.py migrate

# 3) Создать суперпользователя (по желанию)
python manage.py createsuperuser

# 4) Запустить сервер
python manage.py runserver
