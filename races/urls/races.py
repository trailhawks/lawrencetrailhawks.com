from django.conf.urls.defaults import *
import datetime
from lawrencetrailhawks.races.models import Race, Racer


race_info_dict = {
    'queryset': Race.objects.all(),
    'date_field': 'start_datetime',
    'allow_future': True,
    'extra_context': {'upcoming_races': Race.objects.filter(start_datetime__gt=datetime.datetime.today()),
                      'completed_races': Race.objects.filter(start_datetime__lte=datetime.datetime.today()).order_by('-start_datetime'),},
}

racer_info_dict = {
    'queryset': Racer.objects.all(),
}

urlpatterns = patterns('',
    (r'^$',
     'django.views.generic.date_based.archive_index',
     race_info_dict,
     'race_archive_index'),
    (r'^(?P<year>\d{4})/$',
     'django.views.generic.date_based.archive_year',
     race_info_dict,
     'race_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'django.views.generic.date_based.archive_month',
     race_info_dict,
     'race_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'django.views.generic.date_based.archive_day',
     race_info_dict,
     'race_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'django.views.generic.date_based.object_detail',
     race_info_dict,
     'race_detail'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/results', 'races.views.race_result', race_info_dict),
    (r'^results/', 'races.views.results'),
    (r'^upcoming/', 'races.views.upcoming_races'),
    (r'^racers/$',
      'django.views.generic.list_detail.object_list',
      racer_info_dict,
      'racer_list'),
     (r'^racers/(?P<object_id>[-\w]+)/$',
      'django.views.generic.list_detail.object_detail',
      racer_info_dict,
      'racer_detail'),
)
