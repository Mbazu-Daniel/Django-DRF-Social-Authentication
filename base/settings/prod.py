from .common import * 
import os
import dj_database_url

# DEBUG = False
# ALLOWED_HOSTS = ['bazbuy-prod.herokuapp.com']

SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    "default": dj_database_url.config()
}

