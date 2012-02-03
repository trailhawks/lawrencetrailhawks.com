from django.conf import settings
from django.conf.urls.defaults import include
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

from lawrencetrailhawks.lib.Extras import get_latest


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'homepage/homepage.html', 'extra_context': get_latest()}),
    url(r'^blog/', include('lawrencetrailhawks.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^faq/', include('lawrencetrailhawks.faq.urls')),
    url(r'^links/', include('lawrencetrailhawks.links.urls')),
    url(r'^members/', include('lawrencetrailhawks.members.urls')),
    url(r'^photos/', include('lawrencetrailhawks.photos.urls')),
    url(r'^races/', include('lawrencetrailhawks.races.urls')),
    url(r'^runs/', include('lawrencetrailhawks.runs.urls')),

    url(r'^contact/$', 'lawrencetrailhawks.members.views.officer_list'),
    url(r'^member_list/$', 'lawrencetrailhawks.lth.views.member_list'),
    url(r'^sponsors/', 'lawrencetrailhawks.sponsors.views.sponsor_list'),

    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    url(r'^404/$', direct_to_template, {'template': '404.html'}),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
