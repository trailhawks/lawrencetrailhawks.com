from django.conf.urls.defaults import *

from lawrencetrailhawks.runs.models import Runs


runs_info_dict = {
    'queryset': Runs.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
     (r'^$',
     'object_list',
     runs_info_dict,
     'run_object_list'),
    (r'^(?P<slug>[-\w]+)/$',
     'object_detail',
     runs_info_dict,
     'run_detail'),
)
