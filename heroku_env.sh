HEROKU_APP="doc"
DEBUG=True

heroku config:set DEBUG=$DEBUG --app $HEROKU_APP

heroku run python manage.py makemigrations --app $HEROKU_APP
heroku run python manage.py migrate --app $HEROKU_APP
