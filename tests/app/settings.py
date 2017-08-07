import os
import sys

import wagtail.wagtailcore


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
    'captcha',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailforms',
    'wagtail.wagtailimages',
    'wagtail.wagtaildocs',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

wagtail_version = tuple(map(int, wagtail.wagtailcore.__version__.split('.')))

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

    'wagtail.wagtailcore.middleware.SiteMiddleware',
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
