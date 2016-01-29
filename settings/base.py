import os

from unipath import FSPath as Path


PROJECT_ROOT = Path(__file__).ancestor(2)

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Nick Lang', 'nick.lang@example.com'),
)

MANAGERS = ADMINS

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True

USE_ETAGS = True

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = PROJECT_ROOT.child('media_root')
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_ROOT.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    PROJECT_ROOT.child('assets')
]

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# Template stuff
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

# Template stuff
TEMPLATE_LOADERS = [
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
]

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    #'context_processors.base_template_name',
]

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates', 'defaults'),
]

ROOT_URLCONF = 'lawrencetrailhawks.urls.default'

# Middleware
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'waffle.middleware.WaffleMiddleware',
]

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_comments',
    'markup_deprecated',

    'ajaximage',
    'backupdb',
    'django_extensions',
    'django_gravatar',
    'django_thumbor',
    'djrill',
    'favicon',
    'micawber.contrib.mcdjango',
    'rest_framework',
    'robots',
    'shorturls',
    'simple_open_graph',
    'storage_migration',
    'storages',
    'syncr.flickr',
    'syncr.twitter',
    'taggit',
    'waffle',
]

PROJECT_APPS = [
    'blog',
    'core',
    'events',
    'faq',
    'links',
    'locations',
    'members',
    'news',
    'photos',
    'races',
    'runs',
    'sponsors',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            # 'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'lawrencetrailhawks': {
            'handlers': ['console'],
            'level': 'DEBUG',
            # 'filters': ['special']
        }
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SHORT_BASE_URL = 'https://lth.im/'

SHORTEN_MODELS = {
    'B': 'blog.post',
    'E': 'events.event',
    'F': 'faq.faq',
    'L': 'links.links',
    'M': 'members.member',
    'N': 'news.news',
    'R': 'races.race',
    'U': 'runs.run',
}

ALLOWED_HOSTS = [
    'hawkhundred.com',
    '.hawkhundred.com',
    'lawrencetrailhawks.com',
    '.lawrencetrailhawks.com',
    'trailhawks.com',
    '.trailhawks.com',
    'lth.im',
    '.lth.im',
]

MACHINE_TAG_NAMESPACE = 'trailhawks'

# Removing deprecation nagging...
DJANGO_MARKUP_IGNORE_WARNINGS = True

# Favicon path
FAVICON_PATH = STATIC_URL + 'ico/favicon.png'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'PAGINATE_BY_PARAM': 'limit',
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10
}
