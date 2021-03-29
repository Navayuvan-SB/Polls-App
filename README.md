# Polls App

Simple Poll application using Django framework (Python).

## Prerequisite

- Install [Python3](https://www.python.org/downloads/).

- Install latest version of [Django](https://docs.djangoproject.com/en/3.1/topics/install/).

## Steps to run the application

- Clone this [repository](https://github.com/NavayuvanSB/Polls-App).

- Setup PostgreSQL database (change the credentials in `settings.py` if needed).

- Run the database migrations

  ```shell
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Create new superuser if needed.

  ```shell
  python3 manage.py createsuperuser
  ```

- Run the development server
  ```shell
  python3 manage.py runserver
  ```
