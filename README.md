# Crypcentra ICO  API

Written with [Django](https://www.djangoproject.com/) and [DRF](https://www.django-rest-framework.org/)

## Getting started

To start project, run:

```bash
docker-compose up
```

The API will then be available at http://127.0.0.1:8000

## Project commands

Start a new app:

```bash
docker-compose run --rm app sh -c "python manage.py startapp {app_name}"
```

Create superuser:

```bash
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

Makemigrations:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py makemigrations"
```

To migrate:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py migrate"
```

Makemigrations and migrate:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && && python manage.py makemigrations &&python manage.py migrate"
```

Run unit tests:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test"
```

Run linting:

```bash
docker-compose run --rm app sh -c "flake8"
```

Run tests and linting together:

```bash
docker-compose run --rm app sh -c "python manage.py wait_for_db && python manage.py test && flake8"
```

To install new packages:

Add the package name to  ```requirement.txt``` file
then run 

```bash
docker-compose up --build
```

To tear down the all containers:

```bash
docker-compose down
```
