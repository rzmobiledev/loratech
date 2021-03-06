#!/bin/sh

set -e

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
echo "======================================"
echo "LORATECH: YOUR PROJECT IS READY TO GO!"
echo "======================================"

gunicorn --bind :8000 --workers=3 admin.wsgi:application