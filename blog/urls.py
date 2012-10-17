from django.conf.urls.defaults import *

from lawrencetrailhawks.blog.models import Post

blog_info_dict = {
    'queryset': Post.published_objects.all(),
    'date_field': 'publish',
}

blog_draft_info_dict = {
    'queryset': Post.objects.all(),
    'date_field': 'publish',
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.date_based.archive_index', blog_info_dict, 'blog_archive_index'),
    (r'^(?P<year>\d{4})/$', 'django.views.generic.date_based.archive_year', blog_info_dict, 'blog_archive_year'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'django.views.generic.date_based.archive_month', blog_info_dict, 'blog_archive_month'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'django.views.generic.date_based.archive_day', blog_info_dict, 'blog_archive_day'),
    (r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'django.views.generic.date_based.object_detail', blog_draft_info_dict, 'blog_detail'),
)
