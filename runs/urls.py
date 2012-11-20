from django.conf.urls.defaults import *

from .views import RunDetailView, RunListView


urlpatterns = patterns('',
    url(r'^$', RunListView.as_view(), name='run_list'),
    url(r'^(?P<slug>[-\w]+)/$', RunDetailView.as_view(), name='run_detail'),
)
