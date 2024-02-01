# Activate venv environment

python -m venv venv

cd venv/Scripts

source activate

pip install django
pip install djangorestframework

django-admin startproject posts .

python manage.py runserver

python manage.py migrate

python manage.py createsuperuser

go on settings.py add 'posts' into INSTALLED_APPS

then run 

python manage.py makemigrations posts

python manage.py migrate

admin.py ---> register different tables that we want to see on admin panel

on settings.py ---> add on INSTALLED_APPS ---> 'rest_framework'

model -- serializer --endpoint(views.py) ---> urls.py