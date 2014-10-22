from __future__ import absolute_import
from os.path import join, normpath

from .base import *

"""Development settings and globals."""

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
ALLOWED_HOSTS = ['*']
# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION

########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'mediadev'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/mediadev/'
########## END MEDIA CONFIGURATION


########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
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
########## END DATABASE CONFIGURATION


########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
########## END CACHE CONFIGURATION


########## TOOLBAR CONFIGURATION
# See: http://django-debug-toolbar.readthedocs.org/en/latest/installation.html#explicit-setup
INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# http://django-debug-toolbar.readthedocs.org/en/latest/installation.html
INTERNAL_IPS = ('127.0.0.1','0.0.0.0','172.17.156.54')
########## END TOOLBAR CONFIGURATION

########## LOGGING AUTH LDAP
import logging
logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
