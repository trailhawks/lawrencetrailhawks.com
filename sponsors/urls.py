from django.conf.urls import url

from .views import SponsorDetailView, SponsorListView


urlpatterns = [
    url(r'^$', SponsorListView.as_view(), name='sponsor_list'),
    url(r'^(?P<pk>\d+)/$', SponsorDetailView.as_view(), name='sponsor_detail'),
]
