from django.conf import settings
from django_hosts import patterns, host


host_patterns = patterns(
    '',
    #host(r'lawrencetrailhawks\.dev', settings.ROOT_URLCONF, name='without_www'),
    #host(r'www\.lawrencetrailhawks\.dev', settings.ROOT_URLCONF, name='www'),
    host(r'hawkhundred', settings.RACE_URLCONF, name='hawkhundred_race'),
    host(r'hawkhundred\.dev', settings.RACE_URLCONF, name='hawkhundred'),
    host(r'www\.hawkhundred\.dev', settings.RACE_URLCONF, name='hawkhundred_www'),

    host(r'trailhawks\.dev', settings.ROOT_URLCONF, name='default'),
    #host(r'www\.trailhawks\.dev', settings.ROOT_URLCONF, name='trailhawks_www'),
)
