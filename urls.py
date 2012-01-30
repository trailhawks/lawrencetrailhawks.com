from django.conf import settings
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from lawrencetrailhawks.lib.Extras import get_latest


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'homepage.html', 'extra_context': get_latest()}),
    url(r'^blog/', include('lawrencetrailhawks.blog.urls.blog')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^contact/$', 'lawrencetrailhawks.members.views.officer_list'),
    url(r'^faq/', include('lawrencetrailhawks.faq.urls.faq')),
    url(r'^links/', include('lawrencetrailhawks.links.urls.links')),
    url(r'^member_list/$', 'lawrencetrailhawks.lth.views.member_list'),
    url(r'^members/', include('lawrencetrailhawks.members.urls.members')),
    url(r'^photos/', include('lawrencetrailhawks.photos.urls')),
    url(r'^races/', include('lawrencetrailhawks.races.urls')),
    url(r'^runs/', include('lawrencetrailhawks.runs.urls.runs')),
    url(r'^sponsors/', 'lawrencetrailhawks.sponsors.views.get_sponsors'),

    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
