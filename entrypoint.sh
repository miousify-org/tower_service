#!/bin/sh

python manage.py makemigrations jobs; python manage.py migrate

echo "run migrations"

python manage.py runserver 0.0.0.0:80