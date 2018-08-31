import os
import sys

import wagtail.core


def env(name, default=None):
    if sys.version_info < (3,):
        return os.environ.get(name, failobj=default)
    else:
        return os.environ.get(name, default=default)


INSTALLED_APPS = [
    'wagtailformblocks',
    # 'tests.app',

    'taggit',
    'modelcluster',

    'wagtail.core',
    'wagtail.admin',
    'wagtail.users',
    'wagtail.sites',
    'wagtail.contrib.forms',
    'wagtail.images',
    'wagtail.documents',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

wagtail_version = tuple(map(int, wagtail.core.__version__.split('.')))

ROOT_URLCONF = 'tests.app.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': env('DATABASE_NAME', 'test.sqlite3'),
    },
}
SECRET_KEY = 'not so secret'

WAGTAIL_SITE_NAME = 'Wagtail Form Blocks'

DEBUG = True

USE_TZ = True
TIME_ZONE = 'Europe/Amsterdam'

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'
