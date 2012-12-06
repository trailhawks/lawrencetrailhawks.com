from django.conf.urls.defaults import patterns, url

from .views import NewsDetailView, NewsListView


urlpatterns = patterns('',
    url(r'^$', NewsListView.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', NewsDetailView.as_view(), name='news_detail'),
)
