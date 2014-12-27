import os

from unipath import FSPath as Path


#PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__)))
PROJECT_ROOT = Path(__file__).ancestor(1)

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

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT = PROJECT_ROOT.child('media_root')
MEDIA_URL = '/media/'
#MEDIA_URL = 'http://s3.lth.im.s3.amazonaws.com/'

STATIC_ROOT = PROJECT_ROOT.child('static_root')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    PROJECT_ROOT.child('assets')
]

'''
# These are for user-uploaded content.
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media')
MEDIA_URL = '/media/'

# These are for site static media (e.g. CSS and JS)
# This one is where static content is collected to.
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static_root')
STATIC_URL = '/site_media/'
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]
'''

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
    #'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, 'templates'),
]

ROOT_URLCONF = 'lawrencetrailhawks.urls.default'
RACE_URLCONF = 'lawrencetrailhawks.urls.races'

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
    'middleware.QueryRequestUrlMiddleware',
    'django_hosts.middleware.HostsMiddleware',
]

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.messages',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django_comments',
    'markup_deprecated',

    #'djcelery',
    #'gypsy_weather',
    'backupdb',
    'django_extensions',
    'django_gravatar',
    'django_hosts',
    'django_thumbor',
    'djrill',
    'micawber.contrib.mcdjango',
    'shorturls',
    'south',
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

SHORT_BASE_URL = 'http://lth.im/'

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
    'lth.im',
    '.lth.im',
]

MACHINE_TAG_NAMESPACE = 'trailhawks'

#twitter and flickr details left blank, please use your own.
TWITTER = {'username': '', 'password': ''}
FLICKR = {'key': '', 'secret': ''}

# Removing deprecation nagging...
DJANGO_MARKUP_IGNORE_WARNINGS = True

# Root hostconf
DEFAULT_HOST = 'default'
ROOT_HOSTCONF = 'hosts'
