#!/bin/sh

#echo "Running Database Migrations"
#python manage.py makemigrations --noinput
#python manage.py migrate --noinput

echo "Running app commands"
#python manage.py createcachetable
python manage.py collectstatic --noinput &
python manage.py runserver &
exec "$@"