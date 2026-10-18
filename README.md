# Django 05

Учебный проект: один Django проект с тремя приложениями. Каждая вьюха возвращает `HttpResponse`.

## Приложения

| Приложение | Адрес | Что выводит |
|---|---|---|
| `apps/hello/` | `/` | Hello, World! |
| `apps/weekday/` | `/weekday/` | название текущего дня недели |
| `apps/quotes/` | `/quote/` | случайная цитата из списка |

## Стек

- Python 3.12+, Django 5.2
- django-environ — настройки из `.env`

## Структура

```
config/          настройки и главные маршруты
apps/hello/      Hello, World! на главной
apps/weekday/    текущий день недели
apps/quotes/     случайная цитата
```

## Запуск

1. Создать виртуальное окружение и установить зависимости:
   ```
   python -m venv venv
   venv\Scripts\activate          # Windows
   source venv/bin/activate       # Linux / macOS
   pip install -r requirements.txt
   ```

2. Скопировать `.env.example` в `.env` и заполнить значения:
   ```
   DEBUG=True
   SECRET_KEY=любая-длинная-строка
   ```

3. Создать базу данных:
   ```
   python manage.py migrate
   ```

4. Запустить сервер и открыть http://127.0.0.1:8000
   ```
   python manage.py runserver
   ```
