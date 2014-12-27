from django.conf.urls import patterns, url

from .views import SponsorDetailView, SponsorListView


urlpatterns = patterns(
    '',
    url(r'^$', SponsorListView.as_view(), name='sponsor_list'),
    url(r'^(?P<pk>\d+)/$', SponsorDetailView.as_view(), name='sponsor_detail'),
)
