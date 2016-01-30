from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from lawrencetrailhawks.sitemaps.races import StaticViewSitemap


sitemaps = {
    'flatpages': FlatPageSitemap,
    'static': StaticViewSitemap,
}

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    url(r'^faqs/$', TemplateView.as_view(template_name='faqs.html'), name='race_faqs'),
    url(r'^gallery/$', TemplateView.as_view(template_name='gallery.html'), name='race_gallery'),
    url(r'^results/$', TemplateView.as_view(template_name='results.html'), name='race_results'),
    # url(r'^signup/$', TemplateView.as_view(template_name='signup.html'), name='race_signup'),
    # url(r'^travel/$', TemplateView.as_view(template_name='travel.html'), name='race_travel'),

    url(r'^blog/', include('blog.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^races/', include('races.urls')),
    url(r'^runs/', include('runs.urls')),
    url(r'^sponsors/', include('sponsors.urls')),

    url(r'^ajaximage/', include('ajaximage.urls')),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('favicon.urls')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
