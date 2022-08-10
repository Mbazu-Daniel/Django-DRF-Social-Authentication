from .common import * 
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['bizka.herokuapp.com']

SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    "default": dj_database_url.config()
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
