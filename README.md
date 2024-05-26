# Django Project

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Django](https://img.shields.io/badge/Django-4.2-green)
![asgiref](https://img.shields.io/badge/asgiref-3.6.0-red)
![dotenv](https://img.shields.io/badge/dotenv-1.0.1-yellow)
![sqlparse](https://img.shields.io/badge/sqlparse-0.4.3-lightgrey)

Este proyecto es una aplicación web básica creada con Django. Sigue los pasos a continuación para configurar y ejecutar el proyecto en tu entorno local.

## Requisitos

- Python 3.9+
- virtualenv (opcional pero recomendado)

## Instalación

1. **Clona el repositorio:**

    ```bash
    git clone https://github.com/alexisnlh/curso_django_developerpe.git
    cd curso_django_developerpe
    ```

2. **Crea y activa un entorno virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuración

1. **Configura las variables de entorno:**

    Crea un archivo `.env` en el directorio myproject/myproject/ del proyecto (donde se encuentra el settings.py) y añade tus variables de entorno. Ejemplo:

    ```env
    DJANGO_SECRET_KEY = Key secreta del Django settings
    DJANGO_ALLOWED_HOSTS = '["localhost", "127.0.0.1"]'
    ```

    Asegúrate de nunca compartir tu `DJANGO_SECRET_KEY` en un entorno de producción.


2. **Crea las nuevas migraciones para los cambios en los models:**

    ```bash
    python manage.py makemigrations
    ```

3. **Realiza las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

## Uso

1. **Correr el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

2. **Crear un superusuario para el panel de administración:**

    ```bash
    python manage.py createsuperuser
    ```

3. **Acceder a la aplicación:**

    Abre tu navegador y ve a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

    Recuerda que para activar el administrador de Django se debe modificar la variable ADMIN_ENABLED = True en el settings.py, para deshabilitarlo pasaría a False. 

## Librerías Incluidas

- [Django](https://www.djangoproject.com/): Framework web de alto nivel para el desarrollo de aplicaciones rápidas y seguras en Python.
- [asgiref](https://pypi.org/project/asgiref/): Implementación de la especificación ASGI (Asynchronous Server Gateway Interface).
- [python-dotenv](https://pypi.org/project/python-dotenv/): Carga variables de entorno desde un archivo `.env`.
- [sqlparse](https://pypi.org/project/sqlparse/): Biblioteca de análisis y formato de SQL.

## Comandos Útiles

- **Iniciar una shell interactiva de Django:**

    ```bash
    python manage.py shell
    ```

- **Recolección de archivos estáticos:**

    ```bash
    python manage.py collectstatic
    ```
