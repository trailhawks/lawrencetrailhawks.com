from django.conf.urls.defaults import *

from lawrencetrailhawks.races.models import Race, Racer, Result, Report


race_info_dict = {
    'queryset': Race.objects.all(),
    'date_field': 'start_datetime',
}

urlpatterns = patterns('django.views.generic.date_based',
     (r'^$',
     'archive_index',
     race_info_dict,
     'race_archive_index'),
    (r'^(?P<year>\d{4})/$',
     'archive_year',
     race_info_dict,
     'race_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'archive_month',
     race_info_dict,
     'race_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'archive_day',
     race_info_dict,
     'race_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'object_detail',
     race_info_dict,
     'race_detail'),
)
