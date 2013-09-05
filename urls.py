from django.conf.urls.defaults import include, patterns, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from .views import AboutView, HomepageView, ThanksView


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^404/', TemplateView.as_view(template_name='404.html')),
    url(r'^500/', TemplateView.as_view(template_name='500.html')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', 'members.views.officer_list', name='contact'),
    url(r'^contact/thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'^member_list/$', 'members.views.member_list', name='member_list'),
    url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^races/', include('races.urls')),
    url(r'^runs/', include('runs.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
    url(r'^', include('shorturls.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + staticfiles_urlpatterns()
