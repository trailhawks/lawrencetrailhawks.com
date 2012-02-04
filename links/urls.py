from __future__ import absolute_import

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .models import Links


link_info_dict = {
    'queryset': Links.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', link_info_dict, 'link_list'),
    url(r'^(?P<object_id>[-\w]+)/$', 'object_detail', link_info_dict, 'link_detail'),
)
