# What is this
Sky Package Tracking (skypt) is an idea to improve the experience of Sky Staff when receiving packages.

The objective is:
- Easier and faster package registration for the security guard.
- Package arrival notification for the recipient.

# How it should work
0. Package arrives.
0. Security Guard logs in to the application.
0. Security Guard takes photo in application.
0. Security Guard fills in the recipient name.
0. Security Guard confirms Package Registration.
0. Sky Staffer receives notification e-mail (optionally slack).
0. Sky Staffer goes to the Security Guard.
0. Sky Staffer logs in to the application.
0. Sky Staffer marks the package as Retrieve.
0. Security Guard checks Package Retrieve List, compares Package Photo against package and delivers the package to Sky Staffer.

# TODO
- [X] SSL @ramalhais-sky
- [X] Valid SSL Certificate @ramalhais-sky
- [X] Microsoft/Azure sky.uk authentication @ramalhais-sky
- [X] Photo Capture
  - [X] Web @ramalhais-sky
  - [ ] Android
  - [ ] iOS
- [ ] Upload foto
  - [ ] Backend
  - [ ] Web
  - [ ] Firefox @ramalhais-sky
  - [ ] Android
  - [ ] iOS
- [ ] Register package
  - [ ] Backend
  - [ ] Web
  - [ ] Android
  - [ ] iOS
- [ ] List user packages
  - [ ] Backend
  - [ ] Web
  - [ ] Android
  - [ ] iOS
- [ ] Security Guard Login
  - [ ] Backend
  - [ ] Web
  - [ ] Android
  - [ ] iOS
- [ ] Authentication: Register package
- [ ] Authentication: List user packages
- [ ] Android App @sky-philipalmeida
- [ ] iOS App @dfloureiro
- [ ] App notification
  - [ ] Backend
  - [ ] Web
  - [ ] Android
  - [ ] iOS
- [ ] Powerpoint Presentation/Demo

# Nice to Have
- [ ] App running on Docker
- [ ] DB running on Docker
- [ ] App running on IMP/PIQ
- [ ] DB running on IMP/PIQ
- [ ] IMP DNS
- [ ] e-mail notification to user
- [ ] Allow user to add tracking number of an expected package
- [ ] Allow user to add slack username and reveive slack notification
- [ ] Allow user to add tracking number using a bot in slack

# Ideas
- [ ] OCR Name and register package automatically
- [ ] OCR Tracking number and match to a user's expected package
- [ ] Read barcodes,qr codes used in shipping to get the recipient name, phone and tracking number, and register automatically. 
- [ ] Integrate geartrack functionality
- [ ] Sell this product to the world :D

# Notes
- Markdown cheat-sheet
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

## Install latest python
https://www.python.org/downloads/

## Upgrade PIP
```bash
python -m pip install --upgrade pip
```

## MySQL
```bash
pip install mysqlclient
```

## settings.py
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': 'my.cnf',
        },
        'NAME': 'skypt',
        'HOST': os.getenv('MYSQL_HOST'),
        'USER': os.getenv('MYSQL_USER'),
        'PASSWORD': os.getenv('MYSQL_PASSWORD'),
    }
}
TIME_ZONE = 'Europe/Lisbon'
```

```bash
export MYSQL_DB="skypt"
export MYSQL_HOST="localhost"
export MYSQL_USER="skypt"
export MYSQL_PASSWORD="XXX"
```

```mysql
create database skypt;
create user 'skypt'@'%' identified by 'XXX';
grant all privileges on skypt.* to 'skypt'@'%';
```

## Install Django
```bash
python -m pip install Django

python
>>> import django
>>> print(django.get_version())
3.0
```

## Create Django Project and App
```bash
django-admin startproject skypt

cd skypt
python manage.py startapp package_tracking
```

## Setup Django Database
```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser
```bash
python manage.py createsuperuser
```

## HTML photo capture
https://developers.google.com/web/fundamentals/media/capturing-images


# Microsoft/Azure Authentication (SSO)
```bash
pip install django_microsoft_auth
```

## Create app registration in azure
- https://portal.azure.com/
- Home > App registrations > Sky Lisbon Hackathon - SkyPT - Authentication
-  Callback: https://dd.ramalhais.com/microsoft/auth-callback/

## Django Static files
https://docs.djangoproject.com/en/3.0/howto/static-files/

## Django SSL
- https://github.com/teddziuba/django-sslserver
```bash
pip install django-sslserver
```

```
INSTALLED_APPS = (...
"sslserver",
...
)
```

## SSL Certificate (letsencrypt)
- https://zerossl.com/free-ssl/#crt
- https://letsencrypt.org/docs/rate-limits/

## Start HTTPS server with certificate
```bash
python manage.py runsslserver --certificate ../crt --key ../key 0.0.0.0:443
```

## Start HTTPS server with self-signed certificate
```bash
python manage.py runsslserver 0.0.0.0:443
```

## Start HTTP server (no HTTPS/SSL)
```bash
python manage.py runserver 0.0.0.0:80
```
