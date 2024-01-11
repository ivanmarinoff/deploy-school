#!/bin/sh
set -x
#echo "Install the dependencies"
#pip install -r requirements.txt


echo "Running collectstatic commands"
python manage.py collectstatic --noinput &

echo "Running app commands"
python manage.py runserver 0.0.0.0:8000

exec "$@"
