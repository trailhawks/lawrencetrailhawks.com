from django.conf.urls.defaults import patterns, url

from .models import FAQ


faq_info_dict = {
    'queryset': FAQ.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
    url(r'^$', 'object_list', faq_info_dict, 'faq_list'),
    url(r'^(?P<object_id>[-\w]+)/$', 'object_detail', faq_info_dict, 'faq_detail'),
)
