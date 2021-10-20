from .settings import *
import dj_database_url
from decouple import config


# Override defualt setings here

SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
DATABASES = {"default": dj_database_url.config(default=config("DATABASE_URL"))}
