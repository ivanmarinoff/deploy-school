import os
from pathlib import Path

import dj_database_url
from django.conf.global_settings import DATABASES
from django.utils.log import RequireDebugTrue, RequireDebugFalse
from django.conf import DEFAULT_STORAGE_ALIAS
from django.template.context_processors import media
from django.urls import reverse_lazy
from dotenv import load_dotenv

# with open("$.env", 'a+') as newenv:
#     newenv.write("\n$varname=$varvalue")
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",

    "sova_school.web",
    "sova_school.content",
    "sova_school.users.apps.UsersConfig",
    "sova_school.global_content",
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
# ASGI_APPLICATION = "sova_school.asgi.application"

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
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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
DEBUG = 'RENDER' not in os.environ

CORS_ALLOWED_ORIGINS: True

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(' ')

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

CSRF_TRUSTED_ORIGINS = [f'http://{x}:80' for x in os.environ.get('ALLOWED_HOSTS', '').split(' ')]

DATABASES = {
    'default': dj_database_url.config(
        conn_max_age=600,
        conn_health_checks=True,
    ),
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.environ.get('DATABASE_NAME', None),
#         'USER': os.environ.get('DATABASE_USER', None),
#         'PASSWORD': os.environ.get('DATABASE_PASSWORD', None),
#         'HOST': os.environ.get('DATABASE_HOST', None),
#         'PORT': os.environ.get('DATABASE_PORT', None),
#     }
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', None)
EMAIL_PORT = os.environ.get('EMAIL_PORT', None)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', None)
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', None)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
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
STATIC_ROOT = BASE_DIR / 'static_files'

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGIN_REDIRECT_URL = reverse_lazy("profile-details")

LOGOUT_REDIRECT_URL = reverse_lazy("home_page")

LOGIN_URL = reverse_lazy("login_user")

AUTH_USER_MODEL = "users.User"

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SECURE_HSTS_SECONDS = 31536000  # Set the desired HSTS duration (e.g., 1 year)
SECURE_HSTS_PRELOAD = True  # Optional: Enable HSTS preload
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Optional: Include subdomains
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {filename} {funcName} {lineno} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{asctime} {levelname} - {message}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': RequireDebugFalse,
        },
        'require_debug_true': {
            '()': RequireDebugTrue,
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
            'formatter': 'simple',
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'api.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'error_file': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'api_error.log'),
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 5,
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['require_debug_false'],
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'sova_school': {
            'handlers': ['console', 'log_file', 'error_file', 'mail_admins'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['mail_admins', 'error_file'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
    'mail_admins': {
        'level': 'ERROR',
        'class': 'django.utils.log.AdminEmailHandler',
        'filters': ['require_debug_false'],
        'formatter': 'verbose',
    },

}
ADMINS = [('Ivan Marinoff', 'ivanmarinoff.studio6@gmail.com')]