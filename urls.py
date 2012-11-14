from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
    (r'^live/$', direct_to_template, {'template': 'live_coverage.html'}),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
    (r'^blog/', include('blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^contact/$', 'members.views.officer_list'),
    (r'^faq/', include('faq.urls')),
    (r'^links/', include('links.urls')),
    (r'^member_list/$', 'members.views.member_list'),
    (r'^members/', include('members.urls')),
    (r'^photos/', include('photos.urls')),
    (r'^races/', include('races.urls')),
    (r'^runs/', include('runs.urls')),
    (r'^sponsors/', 'sponsors.views.get_sponsors'),
    (r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
