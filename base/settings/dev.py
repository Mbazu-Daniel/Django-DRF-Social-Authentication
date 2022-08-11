from .common import * 


SECRET_KEY = "django-insecure-cdw!0jds5be63&n6=*f19$@)6me$8^&)ow*285k+1uotxjew^2"

ALLOWED_HOSTS = []

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bizka",
        "USER": "postgres",
        "PASSWORD": "qwertyuiop",
        "HOST": "localhost",
        "PORT": 5432,
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
