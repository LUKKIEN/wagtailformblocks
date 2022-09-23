import os

INSTALLED_APPS = [
    'wagtailformblocks',

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
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

ROOT_URLCONF = 'tests.app.urls'

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE', 'django.db.backends.postgresql_psycopg2'),
        'NAME': os.getenv('DATABASE_NAME', 'wagtailformblocks'),
        'HOST': os.getenv('DATABASE_HOST', ''),
        'USER': os.getenv('DATABASE_USER', ''),
        'PASSWORD': os.getenv('DATABASE_PASS', ''),
    },
}

SECRET_KEY = 'not so secret'

WAGTAIL_SITE_NAME = 'Wagtail Form Blocks'

DEBUG = True

USE_TZ = True
TIME_ZONE = 'Europe/Amsterdam'

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
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
