from django.conf.urls.defaults import *

from lawrencetrailhawks.links.models import Links

link_info_dict = {
    'queryset': Links.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
     (r'^$',
     'object_list',
     link_info_dict,
     'link_list'),
    (r'^(?P<object_id>[-\w]+)/$',
     'object_detail',
     link_info_dict,
     'link_detail'),
)
