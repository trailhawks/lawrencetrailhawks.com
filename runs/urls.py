from django.conf.urls.defaults import *

from .models import Run


runs_info_dict = {
    'queryset': Run.objects.all(),
}

urlpatterns = patterns('runs.views',
    url(r'^$', 'run_list', name='run_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'run_detail', name='run_detail'),
)
