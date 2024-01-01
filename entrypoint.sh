#!/bin/sh

echo "Running Database Migrations"
python manage.py makemigrations
python manage.py migrate

echo "Running app management commands"
#python manage.py createcachetable
python manage.py collectstatic --noinput
exec "$@"