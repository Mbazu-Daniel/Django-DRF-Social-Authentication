from .common import * 
import dj_database_url


SECRET_KEY = "django-insecure-cdw!0jds5be63&n6=*f19$@)6me$8^&)ow*285k+1uotxjew^2"

ALLOWED_HOSTS = []


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
#     DATABASES = {
#     'default': dj_database_url.config(
#         # Feel free to alter this value to suit your needs.
#         default='postgres://sopxyldlxcmbnt:b6785d645ffb636cfc607c66a521a8ac94db74c132e2c39a7657d76ff2b518af@ec2-44-206-197-71.compute-1.amazonaws.com:5432/d2b7c6sjdtqjo0', conn_max_age=600)
# }



    # STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'