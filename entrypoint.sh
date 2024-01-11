#!/bin/sh
set -x
#echo "Install the dependencies"
#pip install -r requirements.txt


#echo "Running collectstatic commands"
#python manage.py collectstatic --noinput &
set -e
echo "Running app commands"
python manage.py runserver &

exec "$@"
