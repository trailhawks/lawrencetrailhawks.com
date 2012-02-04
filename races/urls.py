from __future__ import absolute_import

import datetime

from django.conf.urls.defaults import patterns, url

from .models import Race
from .models import Racer


race_info_dict = {
    'queryset': Race.objects.all().order_by('last_name', 'first_name'),
    'date_field': 'start_datetime',
    'allow_future': True,
    'extra_context': {'upcoming_races': Race.objects.filter(start_datetime__gt=datetime.datetime.today()).order_by('start_datetime'),
                      'completed_races': Race.objects.filter(start_datetime__lte=datetime.datetime.today()).order_by('-start_datetime'),
                    },
}

racer_info_dict = {
    'queryset': Racer.objects.all().order_by('last_name'),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.date_based.archive_index', race_info_dict, 'race_index'),
    url(r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', race_info_dict, 'race_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', race_info_dict, 'race_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', race_info_dict, 'race_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'races.views.race_detail', race_info_dict, 'race_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/results', 'races.views.race_result', race_info_dict),
    url(r'^results/', 'races.views.results'),
    url(r'^upcoming/', 'races.views.upcoming_races'),
    url(r'^racers/$', 'django.views.generic.list_detail.object_list', racer_info_dict, 'racer_list'),
    url(r'^racers/(?P<object_id>[-\w]+)/$', 'races.views.racer_detail', racer_info_dict, 'racer_detail'),
)
