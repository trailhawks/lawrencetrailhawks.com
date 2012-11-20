from django.conf.urls.defaults import url, patterns

from .views import MemberDetailView, MemberListView


urlpatterns = patterns('',
    url(r'^$', MemberListView.as_view(), name='member_list'),
    url(r'^(?P<pk>\d+)/$', MemberDetailView.as_view(), name='member_detail'),
)
