from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from lawrencetrailhawks.lib.Extras import get_latest
from django.contrib import admin
from syncr.flickr.models import Photo, PhotoSet
admin.autodiscover()

def redirect(url):
    def inner(request):
        return HttpResponseRedirect(url)
    return inner


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', direct_to_template, {'template': 'homepage.html',
                                 'extra_context': get_latest(),
                                }),
    (r'^photos/', include('lawrencetrailhawks.photos.urls.photos')),
    (r'^about/$', direct_to_template, {'template': 'about.html'}),
    (r'^events/', include('lawrencetrailhawks.events.urls.events') ),
    (r'^faq/', include('lawrencetrailhawks.faq.urls.faq') ),
    (r'^links/', include('lawrencetrailhawks.links.urls.links') ),
    (r'^runs/', include('lawrencetrailhawks.runs.urls.runs') ),
    (r'^members/', include('lawrencetrailhawks.members.urls.members') ),
    (r'^sponsors/', include('lawrencetrailhawks.sponsors.urls.sponsors') ),
    (r'^races/', include('lawrencetrailhawks.races.urls.races') ),

)

