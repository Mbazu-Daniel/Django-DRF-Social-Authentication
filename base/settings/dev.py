from .common import * 
import dj_database_url


# SECRET_KEY = "django-insecure-cdw!0jds5be63&n6=*f19$@)6me$8^&)ow*285k+1uotxjew^2"



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME') 

if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': dj_database_url.config(        # Feel free to alter this value to suit your needs.        default='postgresql://postgres:postgres@localhost:5432/mysite',        conn_max_age=600    )}

DATABASES = {}

if DEBUG:
#     DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "bizka",
#         "USER": "postgres",
#         "PASSWORD": "qwertyuiop",
#         "HOST": "localhost",
#         "PORT": 5432,
#     }
# }
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
else:  
    DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='postgres://sopxyldlxcmbnt:b6785d645ffb636cfc607c66a521a8ac94db74c132e2c39a7657d76ff2b518af@ec2-44-206-197-71.compute-1.amazonaws.com:5432/d2b7c6sjdtqjo0', conn_max_age=600)
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# This setting tells Django at which URL static files are going to be served to the user.
# Here, they well be accessible at your-domain.onrender.com/static/...
STATIC_URL = '/static/'
# Following settings only make sense on production and may break development environments.
if not DEBUG:    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'