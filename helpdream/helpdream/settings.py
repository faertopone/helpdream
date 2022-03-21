"""
Django settings for helpdream project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
with open('helpdream/secret_key_my.txt') as f:
    SECRET_KEY = f.read().strip()

# SECRET_KEY = 'django-insecure-b@kx+i@pgjso)ue%mh_5hofkechxcwecc0l*nxcg^6!3m(%2t*'



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
#для документирования в админ панели
    'django.contrib.admindocs',
    'app_helpdream',
    # чтобы числа больише выглядели красиво
    'django.contrib.humanize',
    # Для добавления карты сайта
    'django.contrib.sitemaps',
    'django.contrib.sites',
    # это где пистаь сообщения (типа средактором)
    'ckeditor',
    'ckeditor_uploader',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #Для локализации
    'django.middleware.locale.LocaleMiddleware',
    'helpdream.middleware.time_delta.TimedeltaDays',


]

# в setting обезателньо еще написать
SITE_ID = 1

ROOT_URLCONF = 'helpdream.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'helpdream.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'W-SU'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = [
    ('ru', 'Русский'),
    ('en', 'English'),
]

#где храниться папка с переводом
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

#Тут хранить загруженные файлы
MEDIA_ROOT = os.path.join(BASE_DIR, 'ALL_DATA_FILES')
#ссылка на фаилы
MEDIA_URL = '/ALL_DATA_FILES/'

if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
       ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')



# STATIC_DIR = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [STATIC_DIR]

# Перед collectstatic это раскоментировать а STATIC DIR закоментировать
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
CKEDITOR_UPLOAD_PATH = "uploads/"


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ]
    }
}




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Сколько вермени хранить пользователя в секундах - тут 30 дней
SESSION_COOKIE_AGE = 30 * 24 * 60 * 60


#формат даты разобраться
DATETIME_INPUT_FORMATS = ['%d/%m/%y %H:%M:%S']


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console',
            'level': 'INFO'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'file',
            'filename': 'debug.log'
        }
    },
    'loggers': {
        '': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        }
    }
}

# Проверка отправка почты во вермя теста
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# mail.ru
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = "helpdream2022@mail.ru"
EMAIL_HOST_PASSWORD = "TtxWPf8GRAFM9UtvWj1t"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False


SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER










#оталдка проекта черещ сайт setry,io

import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://2f99323a0ead4cdead2c173786d96f8f@o1136431.ingest.sentry.io/6194491",
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)