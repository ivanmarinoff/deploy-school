#!/bin/sh

echo "Running collect-static commands"
python manage.py collectstatic --noinput &


echo "Running app commands"
python manage.py runserver &
exec "$@"
