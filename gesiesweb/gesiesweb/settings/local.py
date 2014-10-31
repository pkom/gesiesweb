from __future__ import absolute_import
from os.path import join, normpath

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

TEMPLATE_DEBUG = DEBUG

MEDIA_ROOT = normpath(join(SITE_ROOT, 'mediadev'))
MEDIA_URL = '/mediadev/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': get_secret("DB_LOCAL")["ENGINE"],
        'NAME': get_secret("DB_LOCAL")["NAME"],
        'USER': get_secret("DB_LOCAL")["USER"],
        'PASSWORD': get_secret("DB_LOCAL")["PASSWORD"],
        'HOST': get_secret("DB_LOCAL")["HOST"],
        'PORT': get_secret("DB_LOCAL")["PORT"],       
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

INTERNAL_IPS = ('127.0.0.1','0.0.0.0','172.17.156.54')

########## LOGGING AUTH LDAP
import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
