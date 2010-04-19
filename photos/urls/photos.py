from django.conf.urls.defaults import *
import datetime
from syncr.flickr.models import Photo
from syncr.flickr.views import flickr_photo_detail_in_set as photo_detail

photo_info_dict = {
    'queryset': Photo.objects.all(),
    'date_field': 'taken_date',
}

urlpatterns = patterns('',
    (r'^$', ('lawrencetrailhawks.photos.views.photo_test1')),
    (r'^(?P<year>\d{4})/$',
     'django.views.generic.date_based.archive_year',
     photo_info_dict,
     'race_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$',
     'django.views.generic.date_based.archive_month',
     photo_info_dict,
     'race_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$',
     'django.views.generic.date_based.archive_day',
     photo_info_dict,
     'race_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[\w-]+)/$', photo_detail, 
     name='photo_detail')
)
