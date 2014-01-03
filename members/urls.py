from django.conf.urls import patterns, url

from .views import MemberDetailView, MemberEmailPreview, MemberListView


urlpatterns = patterns('',
    url(r'^$', MemberListView.as_view(), name='member_list'),
    url(r'^preview/$', MemberEmailPreview.as_view(), name='member_email_preview'),
    url(r'^(?P<pk>\d+)/$', MemberDetailView.as_view(), name='member_detail'),
)
