from .base import *

env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool('DEBUGG', default=False)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j)b73=p32@!h4asz^nt0aad&b5kybvg1dmwiqj&lsk4_l4bay-ebc'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
