from django.conf.urls.defaults import *
from lawrencetrailhawks.runs.models import Run

runs_info_dict = {
    'queryset': Run.objects.all(),
}

urlpatterns = patterns('lawrencetrailhawks.runs.views',
    (r'^$', 'run_list'),
    (r'^(?P<slug>[-\w]+)/$', 'run_detail'),
)
