#!/bin/sh

echo "Running app commands"
python manage.py collectstatic --noinput
python manage.py runserver &
exec "$@"
