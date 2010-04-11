from django.conf.urls.defaults import *

from lawrencetrailhawks.members.models import Member


members_info_dict = {
    'queryset': Member.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    (r'^$', 'object_list', members_info_dict, 'member_list'),
    (r'^(?P<object_id>[-\w]+)/$', 'object_detail', members_info_dict, 'member_detail'),
)
