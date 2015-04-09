from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^$', views.PhotoListView.as_view(), name='photo_list'),
    url(r'^review/$', views.PhotoReview.as_view(), name='photo_review_list'),
    url(r'^groups/$', views.PhotoSetListView.as_view(), name='photoset_list'),
    url(r'^(?P<slug>[-_\w]+)/$', views.PhotoDetailView.as_view(), name='photo_detail'),
    url(r'^groups/(?P<flickr_id>[-_\w]+)/$', views.PhotoSetDetailView.as_view(), name='photoset_detail'),
)
