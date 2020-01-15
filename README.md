# install latest python https://www.python.org/downloads/

# upgrade pip
python -m pip install --upgrade pip

#MySQL
pip install mysqlclient

CREATE DATABASE <dbname> CHARACTER SET utf8;

# settings.py
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

export MYSQL_DB="skypt"
export MYSQL_HOST="localhost"
export MYSQL_USER="skypt"
export MYSQL_PASSWORD="XXX"

# Install mysql
create database skypt;
create user 'skypt'@'%' identified by 'XXX';
grant all privileges on skypt.* to 'skypt'@'%';


# Django
python -m pip install Django

python
>>> import django
>>> print(django.get_version())
3.0


django-admin startproject skypt

cd skypt
python manage.py startapp package_tracking
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
admin XXX

# HTML
https://developers.google.com/web/fundamentals/media/capturing-images


# Auth
pip install django_microsoft_auth

# SSL
# https://github.com/teddziuba/django-sslserver
pip install django-sslserver

INSTALLED_APPS = (...
"sslserver",
...
)

python manage.py runsslserver --certificate /path/to/certificate.crt --key /path/to/key.key 0.0.0.0:443
