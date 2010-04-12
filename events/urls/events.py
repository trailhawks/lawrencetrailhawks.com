from django.conf.urls.defaults import *
from lawrencetrailhawks.results.models import Race
import datetime

event_info_dict = {
    'queryset': Race.objects.filter(date__gt=datetime.datetime.now()).order_by('-date'),
    'date_field': 'date',
    'allow_future': True,
}
print event_info_dict
urlpatterns = patterns('django.views.generic.date_based',
     (r'^$',
     'archive_index',
     event_info_dict,
     'event_archive_index'),
    (r'^(?P<year>\d{4})/$',
     'archive_year',
     event_info_dict,
     'event_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'archive_month',
     event_info_dict,
     'event_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'archive_day',
     event_info_dict,
     'event_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$',
     'object_detail',
     event_info_dict,
     'event_detail'),
)