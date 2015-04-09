from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'(lawrencetrailhawks|lth|trailhawks)\.(com|dev|im)', settings.ROOT_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_',
         name='default'),

    host(r'(alpha|new|www)\.(lawrencetrailhawks|lth|trailhawks)\.(com|dev|im)',
         settings.ROOT_URLCONF, name='default_www'),

    host(r'localhost', settings.ROOT_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_',
         name='localhost'),

    host(r'(?P<slug>[\w\.-]+)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred_race'),

    host(r'hawkhundred\.(com|dev)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred'),

    host(r'(alpha|new|www)\.hawkhundred\.(com|dev)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred_www'),
)
