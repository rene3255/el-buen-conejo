import environ
import os
import cloudinary
import cloudinary.uploader
import cloudinary.api

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# Application definition
env = environ.Env()
environ.Env.read_env()

DEBUG = env.bool("DEBUGG", default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-j)b73=p32@!h4asz^nt0aad&b5kybvg1dmwiqj&lsk4_l4bay-ebc"

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
]
EL_BUEN_CONEJO_APPS = [
    "homepage",
    "users_control",
    "resources",
    "farms",
    "cage",
    "rabbit",
    "doe",
    "buck",
    "diary",
    "mating",
]

THIRD_PARTY_APPS = [
    "cloudinary",
    # Django REST framework
    "rest_framework",
]

INSTALLED_APPS = DJANGO_APPS + EL_BUEN_CONEJO_APPS + THIRD_PARTY_APPS

AUTH_USER_MODEL = "users_control.CustomUser"
AUTHENTICATION_BACKENDS = ["users_control.backends.EmailBackend"]

LOGIN_REDIRECT_URL = "home"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ebc_config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ebc_config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {
            "min_length": 8,
        },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": str(os.environ.get("DB_NAME")),
        "USER": str(os.environ.get("DB_USER")),
        "PASSWORD": str(os.environ.get("DB_PASSWORD")),
        "HOST": str(os.environ.get("DB_HOST")),
        "PORT": os.environ.get("DB_PORT"),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/elbuenconejo_images/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "elbuenconejo_images")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
