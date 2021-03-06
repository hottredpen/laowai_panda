"""
Django settings for laowai_panda project.

Generated by 'django-admin startproject' using Django 3.0a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
from django.utils.translation import ugettext_lazy as _
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from django.utils.translation import ugettext_lazy as _

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9@005@qwlq@g&)4d+3gxssl@-cd*8zu!df!-vu8y=1+8$$=@6f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'jet',
    'modeltranslation',
    'django.contrib.humanize',
    'jet.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django.contrib.sites',
    'colorfield',
    'solo',
    'dbmail',
    'api',
    'accounts',
    'connect',
    'revyoume_club',
    'wechat_django',
    'notification',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
   'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'crequest.middleware.CrequestMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'laowai_panda.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '../templates')],
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

WSGI_APPLICATION = 'laowai_panda.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
# TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
# MEDIA_DIR = os.path.join(BASE_DIR, '../media/')
# STATIC_DIR = os.path.join(BASE_DIR, '../static/')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_DIR = os.path.join(BASE_DIR, '../media/')
MEDIA_ROOT = MEDIA_DIR
SITE_ID = 2

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../staticfiles'),
]

STATIC_ROOT = os.path.join(BASE_DIR, '../static/')
AUTH_USER_MODEL ='accounts.User'


###JET CONFIGURATION###
"""
JET THEMES
default
green
light-violet
light-green
light-blue
light-gray
"""
JET_DEFAULT_THEME = 'light-violet'
#######################

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}
LOCALE_PATHS = (os.path.join(BASE_DIR, '../locale'),)

LANGUAGES = (
    ('ar', _('Arabic')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fa', _('Persian')),
    ('fr', _('French')),
    ('hi', _('Hindi')),
    ('id', _('Indonesian')),
    ('it', _('Italian')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('my', _('Malaysian')),
    ('pt', _('Portuguese')),
    ('ru', _('Russian')),
    ('th', _('Thai')),
    ('tr', _('Turkish')),
    ('ur', _('Urdu')),
    ('vi', _('vietnam')),
    ('zh-hans', _('Simplified Chinese')),
    ('zh-hant', _('Traditional Chinese')),
)

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000

JET_INDEX_DASHBOARD = 'laowai_panda.dashboard.MyDefaultIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'jet.dashboard.dashboard.DefaultAppIndexDashboard' 