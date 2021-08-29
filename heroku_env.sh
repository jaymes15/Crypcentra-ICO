HEROKU_APP="crypcentra-ico"
DEBUG=True
DJANGO_SECRET_KEY="django-insecure-l#)^&_&=#0o0*iinf!q2m^-@y@i8se0uea+026#%-ssdjhlq"
ALLOWED_HOST="*"
SETTINGS_MODULE="app.settings_dev"


heroku config:set DEBUG=$DEBUG --app $HEROKU_APP
heroku config:set ALLOWED_HOSTS=$ALLOWED_HOST --app $HEROKU_APP
heroku config:set SECRET_KEY=$DJANGO_SECRET_KEY --app $HEROKU_APP
heroku config:set DJANGO_SETTINGS_MODULE=$SETTINGS_MODULE --app $HEROKU_APP

