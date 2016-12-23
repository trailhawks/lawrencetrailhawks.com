from django.conf.urls import url

from .views import RunDetail, RunList


urlpatterns = [
    url(r'^$', RunList.as_view(), name='run_list'),
    url(r'^(?P<slug>[-\w]+)/$', RunDetail.as_view(), name='run_detail'),
]
