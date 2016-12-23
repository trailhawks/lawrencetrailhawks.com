from django.conf.urls import url

from .views import NewsDetail, NewsList


urlpatterns = [
    url(r'^$', NewsList.as_view(), name='news_list'),
    url(r'^(?P<pk>\d+)/$', NewsDetail.as_view(), name='news_detail'),
]
