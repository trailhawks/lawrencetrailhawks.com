from django.conf.urls.defaults import url, patterns

from lawrencetrailhawks.members.models import Member


members_info_dict = {
    'queryset': Member.objects.all().order_by('last_name', 'first_name'),
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', members_info_dict, 'member_list'),
    url(r'^(?P<object_id>[-\w]+)/$', 'lawrencetrailhawks.members.views.member_detail', members_info_dict, 'member_detail'),
)
