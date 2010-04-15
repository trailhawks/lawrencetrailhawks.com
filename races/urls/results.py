from django.conf.urls.defaults import *

from lawrencetrailhawks.races.models import Race, Racer, Result, Report


result_info_dict = {
    'queryset': Race.objects.all(),
    'date_field': 'start_datetime',
}

print result_info_dict
urlpatterns = patterns('django.views.generic.date_based',
     (r'^$',
     'archive_index',
     result_info_dict,
     'result_archive_index'),
    (r'^(?P<year>\d{4})/$',
     'archive_year',
     result_info_dict,
     'result_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'archive_month',
     result_info_dict,
     'result_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'archive_day',
     result_info_dict,
     'result_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'object_detail',
     result_info_dict,
     'result_detail'),
)
