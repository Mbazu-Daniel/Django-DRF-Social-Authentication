from .common import * 
import dj_database_url


SECRET_KEY = "django-insecure-cdw!0jds5be63&n6=*f19$@)6me$8^&)ow*285k+1uotxjew^2"


DEBUG = True

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "oldBizka",
#         "USER": "postgres",
#         "PASSWORD": "qwertyuiop",
#         "HOST": "localhost",
#         "PORT": 5432,
#     }
# }

ALLOWED_HOSTS  = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {}

if DEBUG:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
else: 
    DATABASES = {
        "default": dj_database_url.config()
    }

