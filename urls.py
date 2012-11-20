from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.simple import direct_to_template


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', direct_to_template, {'template': 'homepage.html'}),
    url(r'^about/$', direct_to_template, {'template': 'about.html'}),
    url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^contact/$', 'members.views.officer_list'),
    url(r'^faq/', include('faq.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^member_list/$', 'members.views.member_list'),
    url(r'^members/', include('members.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^races/', include('races.urls')),
    url(r'^runs/', include('runs.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
    url(r'^thanks/$', direct_to_template, {'template': 'thanks.html'}),
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
