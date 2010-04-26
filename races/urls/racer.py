from django.conf.urls.defaults import *
from lawrencetrailhawks.races.models import Racer


urlpatterns = patterns('',
     (r'^$', 'races.views.get_racer'),
)