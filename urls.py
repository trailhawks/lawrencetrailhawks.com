from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
    (r'^live/$', direct_to_template, {'template': 'live_coverage.html'}),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
    (r'^blog/', include('lawrencetrailhawks.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^contact/$', 'lawrencetrailhawks.members.views.officer_list'),
    (r'^faq/', include('lawrencetrailhawks.faq.urls.faq')),
    (r'^links/', include('lawrencetrailhawks.links.urls.links')),
    (r'^member_list/$', 'lawrencetrailhawks.lth.views.member_list'),
    (r'^members/', include('lawrencetrailhawks.members.urls')),
    (r'^photos/', include('lawrencetrailhawks.photos.urls.photos')),
    (r'^races/', include('lawrencetrailhawks.races.urls')),
    (r'^runs/', include('lawrencetrailhawks.runs.urls')),
    (r'^sponsors/', 'lawrencetrailhawks.sponsors.views.get_sponsors'),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
