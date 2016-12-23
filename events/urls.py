from django.conf.urls import url

from .views import EventDetailView, EventListView


urlpatterns = [
    url(r'^$', EventListView.as_view(), name='event_list'),
    url(r'^(?P<slug>[-\w]+)/$', EventDetailView.as_view(), name='event_detail'),
]
