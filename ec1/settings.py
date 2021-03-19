"""
Django settings for ec1 project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wybye8df00_q)x=@b$sibz*s=x)n$*pc6$qaaok9vm(q3!+hy+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "shop",
    'search_app',
    'cart',
    'stripe',
    "order",
    'crispy_forms',
    'django.contrib.humanize',
    'purchase',
]

### Stripe Settings###
# 公開キー
STRIPE_PUBLISHABLE_KEY = 'pk_test_51INrEmDYWRtgxnI5bKNutTqsylocbo56vp7IHiGYcLsuF5qsKcVLkm4K7NdtqhaQIZSafCTfEirQnbbTnPCYyIoM00LemwOdx5'
# シークレットキー
STRIPE_SECRET_KEY = 'sk_test_51INrEmDYWRtgxnI5BUshqEGH8mpWXMRc0lNAz8otx0ZcuhotWz0GmPhyUzu3SnuaWkLBD3WO9I1H91bt7qrqgdod00w58QHXTv'
STRIPE_WEBHOOK_SECRET = ""

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ec1.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'shop', 'templates/'), os.path.join(BASE_DIR, 'search_app', 'templates/'), os.path.join(BASE_DIR, 'cart', 'templates/'),
            os.path.join(BASE_DIR, 'order', 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shop.context_processors.menu_links',
                'cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'ec1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        )
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')


CRISPY_TEMPLATE_PACK = 'bootstrap4'
NUMBER_GROUPING = 3
THOUSAND_SEPARATOR = ","
USE_THOUSAND_SEPARATOR = True



email_adress = "kintai@kumagaicorp.jp"
email_password = "kotkot1106"

EMAIL_HOST = "sv7514.xserver.jp"
EMAIL_PORT = 465
EMAIL_HOST_USER = email_adress
EMAIL_HOST_PASSWORD = email_password
EMAIL_USE_SSL = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# for email debug settings
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
