from __future__ import absolute_import

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url

from .models import Run


runs_info_dict = {
    'queryset': Run.objects.all(),
}

urlpatterns = patterns('runs.views',
    url(r'^(?P<slug>[-\w]+)/$', 'run_detail', name='run_detail'),
    url(r'^$', 'run_list'),
)
