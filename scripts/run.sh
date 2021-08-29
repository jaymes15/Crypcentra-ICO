#!/bin/sh

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py send_token

uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi