from .common import * 
import os
import dj_database_url

DEBUG = False
# ALLOWED_HOSTS = ['bizka.herokuapp.com', "bizka.onrender.com", "bizka.vercel.com", "127.0.0.1:8001", "localhost:8001", "127.0.0.1:3000", "localhost:3000"]
ALLOWED_HOSTS = ["*"]

SECRET_KEY = os.environ['SECRET_KEY']


DATABASES = {
    "default": dj_database_url.config()
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
