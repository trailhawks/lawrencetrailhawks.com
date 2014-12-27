from django.conf.urls import patterns, url

from .views import EventDetailView, EventListView


urlpatterns = patterns(
    '',
    url(r'^$', EventListView.as_view(), name='event_list'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),
)
