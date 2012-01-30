
#import sys
#sys.path.append('/usr/local/django/')

import logging, os
logging.basicConfig(level = logging.WARN,)


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seabirds',
        'PASSWORD': '9b10c7d8'
    }
}



TIME_ZONE = 'Pacific/Auckland'
LANGUAGE_CODE = 'en-nz'
USE_I18N = True
MEDIA_ROOT = '/usr/local/django/seabirds.net/media/'
MEDIA_URL = ''

ADMIN_MEDIA_PREFIX = '/am/'

SECRET_KEY = 'vtc+y0G^ja;p19874356GHbakhhaayaya987'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    'seabirds.cms.views.get_base_navigation',
    'seabirds.admin.context_processors.whereami',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
)

ROOT_URLCONF = 'seabirds.urls'

TEMPLATE_DIRS = (
    '/usr/local/django/seabirds.net/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.markup',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'seabirds.cms',
    'bibliography',
    'django.contrib.admin',
    'profiles', #Django profiles
    'profile', #App for storing user info
    'taggit',
    'mptt',
    'disqus',
    'reversion',
    'license',
    'django_countries',
)


AUTH_PROFILE_MODULE = 'profile.UserProfile'

if DEBUG == True:
    SITENAME ="development"
    SITE_NAME = 'Seabirds.net website'
    SITE_URL = 'http://localhost:8000'
    SITE_ID = 1
else:
    SITENAME = "Seabirds.net"
    SITE_NAME = 'Seabirds.net website'
    SITE_URL = 'http://seabirds.net'
    SITE_ID = 2
FROM_ADDRESS = 'web@seabirds.net'

INTERNAL_IPS = ('127.0.0.1',)
DISQUS_API_KEY = 'LZG4ehRCHVeOofUobfHU5TDWhtsC3o4UDnJHkGrwo0OmWtwtHpb46q7A8ebDUUFF'
DISQUS_WEBSITE_SHORTNAME = 'seabirds'


EMAIL_HOST = 'localhost'
SUPPORT_EMAIL = 'Finlay Thompson <finlay@dragonfly.co.nz>'

try:
    from sitesettings import *
except ImportError:
    pass

CUCKOO_DIRECTORY = '/usr/local/django/seabirds.net/patches'

# Required for enforcing a global login during testing
LOGIN_URL = '^login'

AVATAR_CROP_MIN_SIZE = 20
