from django.conf.urls.defaults import patterns, url

from . import views
from .feeds import RaceFeed


urlpatterns = patterns('',
    url(r'^$', views.RaceIndex.as_view(), name='race_index'),
    url(r'^(?P<year>\d{4})/$', views.RaceYear.as_view(), name='race_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', views.RaceMonth.as_view(), name='race_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', views.RaceDay.as_view(), name='race_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.RaceDateDetail.as_view(), name='race_detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/results/$', views.RaceResultDetail.as_view(), name='race_result_detail'),
    url(r'^racers/$', views.RacerListView.as_view(), name='racer_list'),
    url(r'^racers/(?P<pk>[-\w]+)/$', views.RacerDetailView.as_view(), name='racer_detail'),
    url(r'^ical/$', RaceFeed(), name='race_ical'),
)
