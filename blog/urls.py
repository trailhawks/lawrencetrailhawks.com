from django.conf.urls.defaults import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.PostArchive.as_view(), name='blog_archive_index'),
    #url(r'^(?P<year>\d{4})/$', views.PostYearArchive.as_view(), name='blog_archive_year'),
    #url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', views.PostMonthArchive.as_view(), name='blog_archive_month'),
    #url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', views.PostDayArchive.as_view(), name='blog_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', views.PostDateDetail.as_view(), name='blog_detail'),
)
