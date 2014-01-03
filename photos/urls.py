from django.conf.urls import patterns, url

from .views import PhotoDetailView, PhotoListView


urlpatterns = patterns('',
    url(r'^$', PhotoListView.as_view(), name='photo_list'),
    url(r'^(?P<slug>[-_\w]+)/$', PhotoDetailView.as_view(), name='photo_detail'),
)
