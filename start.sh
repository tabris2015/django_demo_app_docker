#!/bin/sh
sleep 10
python manage.py migrate
python manage.py collectstatic
python manage.py runscript poblar_db
gunicorn --workers 3 --bind 0.0.0.0:8000 laboratorio.wsgi:application