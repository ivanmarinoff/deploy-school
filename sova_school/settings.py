import os
from pathlib import Path

from django.conf import DEFAULT_STORAGE_ALIAS
from django.template.context_processors import media
from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "channels",
    "rest_framework",
    "rest_framework.authtoken",

    "sova_school.web",
    "sova_school.content",
    "sova_school.users.apps.UsersConfig",
    "sova_school.global_content",
    "sova_school.chat",
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
WSGI_APPLICATION = "sova_school.wsgi.application"
ASGI_APPLICATION = "sova_school.asgi.application"

CACHES = {
    'default': {
        'BACKEND':
            'django.core.cache.backends.db.DatabaseCache',
        'LOCATION':
            'app_cache_table',
    }
}

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "sova_school.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates',
                 'rtmp'],
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

SECRET_KEY = os.environ.get('SECRET_KEY', None)
DEBUG = os.environ.get('DEBUG', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')
CSRF_TRUSTED_ORIGINS = [f'http://{x}:80' for x in os.environ.get('ALLOWED_HOSTS', '').split(' ')]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DATABASE_NAME', None),
        'USER': os.getenv('DATABASE_USER', None),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', None),
        'HOST': os.getenv('DATABASE_HOST', None),
        'PORT': os.getenv('DATABASE_PORT', None),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', None)
EMAIL_PORT = os.getenv('EMAIL_PORT', None)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    # },
    # {
    #     "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    # },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = os.environ.get('STATIC_ROOT', BASE_DIR / 'static_files')

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = reverse_lazy("profile-details")

LOGOUT_REDIRECT_URL = reverse_lazy("home_page")

LOGIN_URL = reverse_lazy("login_user")

AUTH_USER_MODEL = "users.User"

CRISPY_TEMPLATE_PACK = 'bootstrap4'
