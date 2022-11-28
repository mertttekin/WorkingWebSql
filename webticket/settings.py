"""
Django settings for webticket project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from os import getenv
from pathlib import Path
import environ


env = environ.Env()

environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# aşağıda 3 parametre prodoction mode için ayarlandı
SECRET_KEY = 'django-insecure-r#w!b0abs31+jkzv2%6j9fl5pr@aroo&6hnb84=j6$ixf)6t!2'
# SECRET_KEY = getenv("SECRET_KEY")


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = getenv("IS_DEVELOPMENT", True)

# ALLOWED_HOSTS = ["172.16.54.192"]

ALLOWED_HOSTS = ["*"]

# ALLOWED_HOSTS = [
#     getenv("APP_HOST")
# ]

# EmailProject/settings.py #

# Bottom of the file
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = env('EMAIL_HOST')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

RECIPIENT_ADDRESS = env('RECIPIENT_ADDRESS')


# Application definition



CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            ['Undo', 'Redo',
             '-', 'Bold', 'Italic', 'Underline',
             '-', 'Link', 'Unlink', 'Anchor',
             '-', 'Format',

             '-', 'Maximize',

             ],
        ],
        'width': 'auto',
        'toolbarCanCollapse': True,
    },
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_userforeignkey',
    'crispy_forms',
    'rest_framework',
    'account',
    'tickets',
    'ckeditor',
    'api',
    'phonenumbers',
    'django_mobile',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_userforeignkey.middleware.UserForeignKeyMiddleware',
]


ROOT_URLCONF = 'webticket.urls'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'webticket.wsgi.application'


# SQLite database information

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

#Production database information

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'webticket',
        'USER': 'merttekin',
        'PASSWORD': 'smartmed1a',
        'HOST': 'webticket-2.ceiungwlltpc.eu-central-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

#Development database information

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'webticket',
#         'USER': 'postgres',
#         'PASSWORD': 'merttekin',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }


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

LANGUAGE_CODE = 'tr-tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / 'static']

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_ROOT = BASE_DIR / "uploads"

# STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")

MEDIA_URL = "/images/"
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'




# DATABASES['default'] =  dj_database_url.config()

MIDDLEWARE_CLASSES = (
    # Other middleware classes go here
    'django_mobile.middleware.MobileDetectionMiddleware',
    'django_mobile.middleware.SetFlavourMiddleware',
    'responsive.middleware.DeviceInfoMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Other context processors included here
    'django_mobile.context_processors.flavour',
    'responsive.context_processors.device_info',
)

TEMPLATE_LOADERS = (
    'django_mobile.loader.Loader',
)

# Name, Max Width (inclusive)
