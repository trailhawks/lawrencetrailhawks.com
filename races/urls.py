from django.conf.urls import url

from . import views
from .feeds import RaceFeed


urlpatterns = [
    url(r'^$', views.RaceIndex.as_view(), name='race_index'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.RaceDateDetail.as_view(), name='race_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/results/$', views.RaceResultDetail.as_view(), name='race_result_detail'),
    url(r'^ical/$', RaceFeed(), name='race_ical'),
    url(r'^racers/(?P<pk>[-\w]+)/$', views.RacerDetail.as_view(), name='racer_detail'),
]
