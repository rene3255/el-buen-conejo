from .base import *
from pathlib import Path
import environ
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool('DEBUGG', default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j)b73=p32@!h4asz^nt0aad&b5kybvg1dmwiqj&lsk4_l4bay-ebc'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(os.environ.get('DB_NAME')),
        'USER': str(os.environ.get('DB_USER')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD')),
        'HOST':str(os.environ.get('DB_HOST')),
        'PORT':os.environ.get('DB_PORT'),
    }
}

