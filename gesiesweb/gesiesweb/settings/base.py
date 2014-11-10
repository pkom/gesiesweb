#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
import json
from sys import path
from os.path import abspath, basename, dirname, join, normpath

from django.core.exceptions import ImproperlyConfigured

"""Common settings and globals."""

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

########## LOAD JSON SETTINGS
with open(join(DJANGO_ROOT, "settings","settings.json")) as f:
    try:
        secrets = json.loads(f.read())
    except (ValueError, KeyError, TypeError):
        print "JSON format error"

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)
########## END LOAD JSON SETTINGS

SITE_ROOT = dirname(DJANGO_ROOT)

SITE_NAME = basename(DJANGO_ROOT)

path.append(DJANGO_ROOT)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

DEBUG = False

TEMPLATE_DEBUG = DEBUG

ADMINS = (
          get_secret("ADMIN"), get_secret("ADMIN_EMAIL"),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': get_secret("DB_BASE")["ENGINE"],
        'NAME': get_secret("DB_BASE")["NAME"],
        'USER': get_secret("DB_BASE")["USER"],
        'PASSWORD': get_secret("DB_BASE")["PASSWORD"],
        'HOST': get_secret("DB_BASE")["HOST"],
        'PORT': get_secret("DB_BASE")["PORT"],
    }
}

TIME_ZONE = 'Europe/Madrid'

LANGUAGE_CODE = 'es-es'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))
MEDIA_URL = '/media/'

STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    normpath(join(SITE_ROOT, 'static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = get_secret("SECRET_KEY")

ALLOWED_HOSTS = []

FIXTURE_DIRS = (
    normpath(join(SITE_ROOT, 'fixtures')),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',

    # app context processor
    'core.context_processors.append_data',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    normpath(join(SITE_ROOT, 'templates')),
)

MIDDLEWARE_CLASSES = (
    # Default Django middleware.
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '%s.urls' % SITE_NAME

DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Useful template tags:
    # 'django.contrib.humanize',
    # Admin panel and documentation:
    'django.contrib.admin',
    # 'django.contrib.admindocs',
    'sorl.thumbnail',
    'rest_framework',
)

LOCAL_APPS = (
    'core',
    'rayuela',
    'config',
    'cursos',
    'alumnos',
    'profesores',
    'grupos',
    'departamentos',
    'asignaturas',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

INSTALLED_APPS += (

)

LOGIN_URL = '/core/login'
LOGOUT_URL = '/core/logout'

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}


########## DJANGO-AUTH-LDAP CONFIGURATION
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

AUTH_LDAP_SERVER_URI = get_secret("AUTH_LDAP_SERVER_URI")
AUTH_LDAP_START_TLS = True

# Autenticacion por usuario django
AUTH_LDAP_BIND_DN = get_secret("AUTH_LDAP_BIND_DN")
AUTH_LDAP_BIND_PASSWORD = get_secret("AUTH_LDAP_BIND_PASSWORD")
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=People,dc=instituto,dc=extremadura,dc=es",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# Autenticacion directa del usuario, pero no obtengo el dni...
#AUTH_LDAP_USER_DN_TEMPLATE = "uid=%(user)s,ou=People,dc=instituto,dc=extremadura,dc=es"

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Group,dc=instituto,dc=extremadura,dc=es",
    ldap.SCOPE_SUBTREE, "(objectClass=groupOfNames)"
)
AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

# Simple group restrictions
AUTH_LDAP_REQUIRE_GROUP = "cn=teachers,ou=Group,dc=instituto,dc=extremadura,dc=es"
AUTH_LDAP_DENY_GROUP = "cn=students,ou=Group,dc=instituto,dc=extremadura,dc=es"

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    #"first_name": "cn",
    #"last_name": "sn"
}

#Esto ya no va en django 1.7
#AUTH_PROFILE_MODULE = 'profesores.Profesor'
#hay que hace algo como
#profile = request.user.profesor

AUTH_LDAP_PROFILE_ATTR_MAP = {
    "dni": "employeeNumber",
    "usuario_rayuela": "uid"
}

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=teachers,ou=Group,dc=instituto,dc=extremadura,dc=es",
    "is_staff": "cn=teachers,ou=Group,dc=instituto,dc=extremadura,dc=es",
#    "is_superuser": "cn=superuser,ou=django,ou=groups,dc=example,dc=com"
}

#AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
#    "is_awesome": "cn=awesome,ou=django,ou=groups,dc=example,dc=com",
#}

# This is the default, but I like to be explicit.
AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Use LDAP group membership to calculate group permissions.
AUTH_LDAP_FIND_GROUP_PERMS = True

# Cache group memberships for an hour to minimize LDAP traffic
#AUTH_LDAP_CACHE_GROUPS = True
#AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
)
########## END DJANGO-AUTH-LDAP CONFIGURATION
