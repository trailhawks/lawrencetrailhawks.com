from django.conf.urls import patterns, url

from .views import NewsDetail, NewsList


urlpatterns = patterns(
    '',
    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail'),
)
