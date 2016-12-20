from django.conf.urls import patterns, url

from .views import FaqDetailView, FaqListView


urlpatterns = patterns('',
    url(r'^$', FaqListView.as_view(), name='faq_list'),
    url(r'^(?P<pk>\d+)/$', FaqDetailView.as_view(), name='faq_detail'),
)
