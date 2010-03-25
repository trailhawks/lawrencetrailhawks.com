from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from lawrencetrailhawks.Extras import get_latest

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

def redirect(url):
    def inner(request):
        return HttpResponseRedirect(url)
    return inner


urlpatterns = patterns('',
    # Example:
    # (r'^lawrencetrailhawks/', include('lawrencetrailhawks.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
	#direct to template
	(r'^$', direct_to_template, {'template': 'homepage.html',
								 'extra_context': get_latest(),
								}),
	(r'^about/$', direct_to_template, {'template': 'about.html'}),
	(r'^events/', include('lawrencetrailhawks.events.urls.events') ),
	(r'^faq/', include('lawrencetrailhawks.faq.urls.faq') ),
	(r'^links/', include('lawrencetrailhawks.links.urls.links') ),
	(r'^runs/', include('lawrencetrailhawks.runs.urls.runs') ),
	(r'^members/', include('lawrencetrailhawks.members.urls.members') ),
	(r'^sponsors/', include('lawrencetrailhawks.sponsors.urls.sponsors') ),
	(r'^results/', include('lawrencetrailhawks.results.urls.results') ),

)

