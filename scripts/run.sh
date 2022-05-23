#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --no-input
python manage.py migrate
python manage.py createsuperuser --no-input --username $SUPERUSER_USERNAME --email $SUPERUSER_EMAIL --password $SUPERUSER_PASSWORD
python manage.py runserver 0.0.0.1:8000