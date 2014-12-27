from django.conf.urls import patterns, url

from .views import LinkDetailView, LinkListView


urlpatterns = patterns(
    '',
    url(r'^$', LinkListView.as_view(), name='link_list'),
    url(r'^(?P<pk>\d+)/$', LinkDetailView.as_view(), name='link_detail'),
)
