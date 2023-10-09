# Документация проекта "Share Stepik"

Добро пожаловать в документацию проекта "Share Stepik", который был сделан для участия в хакатоне от Stepik. Этот проект представляет собой инструмент для пользователей, который способен упорядочивать и систематизровать курсы на платформе. С его помощью можно создавать подборки курсов, а также целые специализации и делиться ими.

[https://rcfixer.pythonanywhere.com/](https://rcfixer.pythonanywhere.com/)

[Пользовательская документация](https://docs.google.com/document/d/1b8mQXCfvEZuNr3hfei3wmMYoc5HzW1NUReTM6k8i4Z0/edit#heading=h.uz5t352f66zc)

## Установка и настройка

1. Установите Python и необходимые зависимости из файла requirements.txt, если они ещё не установлены:

```console
pip install -r requirements.txt
```

2. Клонируйте репозиторий проекта:

```console
git clone https://github.com/RCFixer/share_stepik.git
```

3. Перейдите в директорию проекта:

```console
cd share_stepik
```

4. Запустите миграции:

```console
python manage.py migrate
```

5. Создайте суперпользователя

```console
python manage.py createsuperuser
```

6. Запустите сервер разработки:

```console
python manage.py runserver
```

7. Откройте браузер и перейдите по адресу `http://localhost:8000` для доступа к приложению.


## Модели данных

### Курсы

Модель `Course` используется для хранения информации о курсах платформы Stepik. Она включает в себя следующие поля:

- `title`: заголовок курса (CharField)
- `link`: ссылка на курс (CharField)
- `image_src`: ссылка на изображение курса (CharField)


Модель `SharePage` используется для хранения информации о подборке курсов. Она включает в себя следующие поля:

- `title`: заголовок подборки (CharField)
- `courses`: содержащиеся на странице курсы (ManyToManyField)
- `is_for_specialization`: является ли эта подборка самостоятельной или относится к специализации (BooleanField)
- `specialization`: специализация к которой привязана подборка, если она есть (ForeignKey)
- `likes`: количество лайков подборки (PositiveIntegerField)

Модель `SpecializationPage` используется для хранения информации о специализации. Она включает в себя следующие поля:

- `title`: заголовок специализации (CharField)
- `likes`: количество лайков специализации (PositiveIntegerField)


## Представления (Views)

Проект содержит следующие представления:

- `create_page`: создаёт страницу с подборкой курсов.
- `update_page`: обновляет страницу с подборкой курсов.
- `delete_page`: удаляет страницу с подборкой курсов.
- `page_list`: отображает страницу со всем подборками курсов.
- `page_view`: отображает страницу с одной подборкой курсов.
- `create_specialization`: создаёт страницу со специализацией.
- `specialization_view`: отображает страницу со специализацией.
- `create_specialization_page`: создаёт подборку курсов для конкретной специализации.
- `specialization_page_list`: отображает список всех специализаций.
- `update_specialization_page`: обновляет страницу конкретной специализации.
- `delete_specialization_page`: удаляет страницу конкретной специализации.



## Работа с URL-ами

URL-ы для доступа к представлениям находятся в файле `urls.py` проекта и могут быть настроены по вашим потребностям.



