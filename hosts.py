from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    host(r'lawrencetrailhawks\.(com|dev|im)', settings.ROOT_URLCONF,
         name='default'),

    host(r'(alpha|www)\.lawrencetrailhawks\.(com|dev|im)', settings.ROOT_URLCONF,
         name='default_www'),

    host(r'(?P<race>[\w\.-]+)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred_race'),

    host(r'hawkhundred\.(com|dev)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred'),

    host(r'www\.hawkhundred\.(com|dev)', settings.RACE_URLCONF,
         callback='lawrencetrailhawks.races.callbacks.host_race',
         name='hawkhundred_www'),
)
