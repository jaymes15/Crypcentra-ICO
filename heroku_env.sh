HEROKU_APP="crypcentra-ico"
DEBUG=True

echo "hdhd testunggg"
echo $JAMES

heroku config:set DEBUG=$DEBUG --app $HEROKU_APP

heroku run python manage.py makemigrations --app $HEROKU_APP
heroku run python manage.py migrate --app $HEROKU_APP
