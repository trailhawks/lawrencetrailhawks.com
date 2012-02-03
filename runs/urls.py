from __future__ import absolute_import

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .models import Run


runs_info_dict = {
    'queryset': Run.objects.all(),
}

urlpatterns = patterns('lawrencetrailhawks.runs.views',
    url(r'^$', 'run_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'run_detail'),
)
