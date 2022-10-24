import os
import sys

from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from .base import *  # NOQA

sys.path.append(os.path.join(BASE_DIR, 'apps'))

# SENTRY Integration

SENTRY_DSN = ENV.str('SENTRY_DSN', '')
if SENTRY_DSN:
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],
    )

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ENV.str('SECRET_KEY', 'Keep it secret!')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV.bool('DEBUG', True)
ENABLE_DEBUG_TOOLBAR = DEBUG and ENV.bool('ENABLE_DEBUG_TOOLBAR', False)

ALLOWED_HOSTS = ENV.list('ALLOWED_HOSTS', default=['*'])
INTERNAL_IPS = ENV.list('INTERNAL_IPS', default=('127.0.0.1',))

# Django Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

# 3rd party Application definition

EXTERNAL_APPS = [
    'django_extensions',
    'compressor',
    'django_countries',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',
    'csvexport',
]
SITE_ID = 1

# Local Application definition

LOCAL_APPS = [
    'core',
    'accounts',
    'common',
    'testimonials',
    'portfolios',
    'services',
    'posts',
    'stores',
    'orders',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + LOCAL_APPS
INSTALLED_APPS.insert(0, 'modeltranslation')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# HTTP Basic Authentication settings

ENABLE_HTTP_BASIC_AUTH = ENV.bool('ENABLE_HTTP_BASIC_AUTH', False)
if ENABLE_HTTP_BASIC_AUTH:
    MIDDLEWARE.insert(2, 'core.middleware.BasicAuthMiddleware')

    HTTP_BASIC_AUTH_EXCLUDE_URLS = ()

# Django Debug Toolbar settings
# https://django-debug-toolbar.readthedocs.io/en/stable/configuration.html

if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append('debug_toolbar')
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

    DEBUG_TOOLBAR_CONFIG = {
        'RESULTS_CACHE_SIZE': 50,
        'SHOW_TOOLBAR_CALLBACK': lambda request: DEBUG,
    }

    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.sql.SQLPanel',
    ]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'common.context_processors.company_info',
                'common.context_processors.service_order',
                'common.context_processors.settings',
                'common.context_processors.forms',
                'common.context_processors.social_media',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': ENV.db_url('DATABASE_URL', default='sqlite://:memory:'),
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': '123',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'defaultdb',
        'USER': 'doadmin',
        'PASSWORD': 'AVNS_bfzrd5bCf7FbJ1zG7zY',
        'HOST': 'crepixa-db-postgresql-do-user-11307117-0.b.db.ondigitalocean.com',
        'PORT': '25060',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        },
    },
]

# User settings
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
LOGIN_URL = reverse_lazy('common:homepage')
LOGIN_REDIRECT_URL = reverse_lazy('common:homepage')
LOGOUT_REDIRECT_URL = reverse_lazy('common:homepage')

# AllAuth settings

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = False

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('ar', 'العربية'),
    ('de', 'Deutsch'),
    ('fr', 'Français'),
]
MODELTRANSLATION_LANGUAGES = ['en', 'ar', 'de', 'fr']
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'collectstatic')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)
COMPRESS_ENABLED = ENV.bool('COMPRESS_ENABLED', False)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
CKEDITOR_UPLOAD_PATH = '/media/uploads/'

# Email settings

EMAIL_BASE_TEMPLATE = 'email/base.html'
EMAIL_HOST = ENV.str('EMAIL_HOST', 'localhost')
EMAIL_PORT = ENV.int('EMAIL_PORT', 25)
EMAIL_HOST_USER = ENV.str('EMAIL_HOST_USER', '')
DEFAULT_FROM_EMAIL = ENV.str('DEFAULT_FROM_EMAIL', 'no-reply@example.com')
EMAIL_HOST_PASSWORD = ENV.str('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_TLS = ENV.bool('EMAIL_USE_TLS', False)
EMAIL_BACKEND = ENV.str('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')

# Site settings

SITE_NAME = ENV.str('SITE_NAME', 'Django')
CLIENT_DOMAIN = ENV.str('CLIENT_DOMAIN', '127.0.0.1:8000')
URL_SCHEME = ENV.str('URL_SCHEME', 'http')

HTTP_BASIC_AUTH = {
    'crepixa': 'crepixa',
}
ADMIN_EMAILS = [
    'service@crepixa.com',
    'admin@crepixa.com',
    'sanaa@crepixa.com',
    'crepixa@gmail.com',
]

HTTP_BASIC_AUTH_EXCLUDE_URLS = (
    '/social-accounts/facebook/login/callback/',
    '/en/social-accounts/facebook/login/callback/',
    '/ar/social-accounts/facebook/login/callback/',
    '/de/social-accounts/facebook/login/callback/',
    '/social-accounts/google/login/callback/',
    '/en/social-accounts/google/login/callback/',
    '/ar/social-accounts/google/login/callback/',
    '/de/social-accounts/google/login/callback/',
    '/about/',
    '/en/about/',
    '/ar/about/',
    '/de/about/',
)

DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600

# https://github.com/vintasoftware/safari-samesite-cookie-issue
CSRF_COOKIE_SAMESITE = None
SESSION_COOKIE_SAMESITE = None

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
