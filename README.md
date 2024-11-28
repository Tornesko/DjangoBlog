
# DjangoBlog

DjangoBlog is a web application designed for blogging purposes, built using the Django framework. This project allows users to create, edit, and manage blog posts, as well as interact with other users through comments or other features.

## Features

- User authentication (login/logout)
- Blog post creation, editing, and deletion
- Interactive comments system
- Admin panel for site management
- Responsive UI design

## Project Structure

```plaintext
DjangoBlog/
├── blog/
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── [migration files...]
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── add_post.html
│   │   ├── update_post.html
│   │   └── [other templates...]
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── authentication/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── [migration files...]
│   ├── templates/
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── [other templates...]
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
│   ├── images/
│       └── profile/
│           └── [profile images...]
├── db.sqlite3
└── manage.py
```

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (>= 3.8)
- pip (Python package manager)
- Virtualenv (optional, for virtual environment management)

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd DjangoBlog
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser for the admin panel:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

7. Open the application in your browser:

    ```
    http://127.0.0.1:8000/
    ```

## Usage

- Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- Start creating blog posts, manage users, and interact with the site.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any feature requests or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


```plaintext
DjangoBlog/
├── blog/                # Головний додаток блогу
├── config/              # Налаштування Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py      # Основні налаштування
│   ├── urls.py          # Глобальні маршрути
│   └── wsgi.py
├── main/                # Додаток для управління постами
│   ├── migrations/      # Міграції для бази даних
│   │   └── [міграційні файли...]
│   ├── templates/       # Шаблони для рендерингу сторінок
│   │   ├── base.html    # Базовий шаблон
│   │   ├── home.html    # Головна сторінка
│   │   ├── add_post.html # Шаблон створення постів
│   │   ├── update_post.html # Шаблон редагування постів
│   │   └── [інші шаблони...]
│   ├── __init__.py
│   ├── admin.py         # Реєстрація моделей у панелі адміністратора
│   ├── apps.py          # Конфігурація додатка
│   ├── forms.py         # Форми для вводу даних
│   ├── models.py        # Моделі для бази даних
│   ├── tests.py         # Тестування
│   ├── urls.py          # Локальні маршрути додатка
│   └── views.py         # Логіка відображення сторінок
├── authentication/      # Додаток для реєстрації та авторизації
│   ├── migrations/
│   │   └── [міграційні файли...]
│   ├── templates/       # Шаблони для логіна та реєстрації
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   ├── register.html
│   │   │   └── [інші шаблони...]
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/               # Медійні файли
│   ├── images/          # Зображення профілів
│   │   └── profile/
│   │       └── [зображення профілів...]
├── db.sqlite3           # База даних SQLite
└── manage.py            # Командний менеджер Django
