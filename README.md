# Django project setting up (with Django-Ninja)

## 1. Virtual Environment

### Create virtual environment

In directory "Folder 1" using terminal,

`python -m venv venv`

### Activate virtual envionment

- With **Git bash** in **Windows**

`. venv/bin/activate`or `source . venv/bin/activate`

## 2. Django-Ninja

### Install Django-Ninja

In the same directory "Folder 1",

`pip install django-ninja`

## 3. New Django project

In the same directory "Folder 1",

`django-admin startproject config .`

### 4. Create new App in Django project

- create new app in terminal

`python manage.py startapp newapp`

- add the app `config/settings.py`

```
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
'newApp',
]

```

### 5. Run the project

`python manage.py runserver`

---

> The directory will be like:
config/ manage.py newapp/ venv/
>