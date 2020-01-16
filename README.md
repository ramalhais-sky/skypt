# TODO
- [X] SSL
- [X] Valid SSL Certificate 
- [X] Microsoft/Azure sky.uk authentication
- [X] Photo Capture in Chrome and Firefox
- [ ] Upload foto
- [ ] Register package
- [ ] Implement personal package list
- [ ] Security Guard Login
- [ ] Protect Register package
- [ ] Protect personal package list
- [ ] Android App
- [ ] iOS App
- [ ] Powerpoint Presentation/Demo

# Nice to Have
- [ ] App running on Docker
- [ ] App running on IMP/PIQ
- [ ] DB running on IMP/PIQ
- [ ] IMP DNS

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

# Start HTTP server (no HTTPS/SSL)
```bash
python manage.py runserver 0.0.0.0:80
```
