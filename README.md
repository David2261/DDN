# DDN ![GitHub repo size](https://img.shields.io/github/repo-size/David2261/DDN)

## Tools
- Python 3.9
- Django 4.1
- Poetry
- Django-environ
- Flake8
- Docker
- Debian/Linux

## Install
- With poetry/venv
```bash
sudo apt upgrade
poetry install
. .venv/bin/activate
python3 manage.py collectstatic
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
- With Docker
```bash
sudo apt upgrade
docker login
docker build . --tag ddn
docker run -p 8080:8000 ddn # с портом 8080
```

- Root
```bash 
chmod 777 -R .
```

## Task

Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:

1. Меню реализовано через template tag
2. Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3. Хранится в БД.
4. Редактируется в стандартной админке Django
5. Активный пункт меню определяется исходя из URL текущей страницы
6. Меню на одной странице может быть несколько. Они определяются по названию.
7. При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8. На отрисовку каждого меню требуется ровно 1 запрос к БД
   Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
   {% draw_menu 'main_menu' %}
   При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
   При решении тестового задания у вас не должно возникнуть вопросов. Если появляются вопросы, вероятнее всего, у вас недостаточно знаний.
   Задание выложить на гитхаб.

## Example
![Main page](/source/main_page.png)

![Types page](/source/type_page.png)

![Good p](/source/good_page.png)
