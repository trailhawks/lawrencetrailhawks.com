from django.conf.urls import patterns, url

from .views import RunDetail, RunList


urlpatterns = patterns(
    '',
    url(r'^$', RunList.as_view(), name='run_list'),
    url(r'^(?P<slug>[-\w]+)/$', RunDetail.as_view(), name='run_detail'),
)
