""" ---------------------------------------------------------------------------------------
IMPORTANT: manage.py is running in local.py for development. Need to adjust when deploying.

"""

import os
from pathlib import Path

# import sentry_sdk

# from sentry_sdk.integrations.django import DjangoIntegration

# sentry_sdk.init(
#     dsn="https://1d850256131746469d85fe64db2fe3e1@o458567.ingest.sentry.io/5597887",
#     integrations=[DjangoIntegration()],
#     traces_sample_rate=1.0,

#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ['RUNETASK_SECRET_KEY']
# ALLOWED_HOSTS = [
#     'localhost',
#     '127.0.0.1',
# ]
SECRET_KEY = 'sfgggggggggggggdf'

# CORS_ALLOWED_ORIGINS = [
#     'http://127.0.0.1:8000',
#     'http://127.0.0.1:8888',
#     'http://localhost:8888',
#     'http://127.0.0.1:3000',
#     'http://localhost:3000',
# ]



# DEBUG=True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.google',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'rest_framework',
    'rest_framework.authtoken',
    
    'corsheaders',

    'tasks',
    'users',
]

SITE_ID = 1

MIDDLEWARE = [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

CORS_ALLOW_ALL_ORIGINS = True

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

WSGI_APPLICATION = 'config.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
    'facebook': {
         'METHOD': 'oauth2',
         'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
         'SCOPE': ['email', 'public_profile'],
         'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
         'INIT_PARAMS': {'cookie': True},
         'FIELDS': [
             'email',
             'first_name',
             'last_name',
             'name',
             'name_format',
             'picture',
             'short_name',
         ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': False,
        'VERSION': 'v13.0',

         'APP': {
                }
    }
    
}