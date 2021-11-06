heroku config:set DEBUG=$DEBUG_STAGING --app $HEROKU_APP_STAGING

heroku run python manage.py makemigrations --app $HEROKU_APP_STAGING
heroku run python manage.py migrate --app $HEROKU_APP_STAGING
