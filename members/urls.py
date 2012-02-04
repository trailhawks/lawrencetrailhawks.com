from __future__ import absolute_import

from django.conf.urls.defaults import url, patterns

from .models import Member


members_info_dict = {
    'queryset': Member.objects.active().order_by('last_name', 'first_name'),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', members_info_dict, 'member_list'),
    url(r'^(?P<object_id>[-\w]+)/$', 'members.views.member_detail', members_info_dict, 'member_detail'),
)
