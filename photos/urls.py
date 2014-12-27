from django.conf.urls import patterns, url

from .views import PhotoDetailView, PhotoListView, PhotoSetDetailView, PhotoSetListView


urlpatterns = patterns(
    '',
    url(r'^$', PhotoListView.as_view(), name='photo_list'),
    url(r'^groups/$', PhotoSetListView.as_view(), name='photoset_list'),
    url(r'^(?P<slug>[-_\w]+)/$', PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^groups/(?P<flickr_id>[-_\w]+)/$', PhotoSetDetailView.as_view(), name='photoset_detail'),
)
