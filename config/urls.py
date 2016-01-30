from __future__ import absolute_import

from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import FlatPageSitemap, GenericSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from lawrencetrailhawks.sitemaps.default import StaticViewSitemap
from lawrencetrailhawks.views import (
    AboutView,
    HomepageView,
    HumansView,
    StyleGuideView,
    ThanksView,
)
from blog.models import Post
from news.models import News
from races.models import Race
from photos.apis import PhotoViewSet, RandomPhotoViewSet


blog_dict = {
    'queryset': Post.objects.public(),
    'date_field': 'publish',
}

news_dict = {
    'queryset': News.objects.public(),
    'date_field': 'pub_date',
}

race_dict = {
    'queryset': Race.objects.all(),
    'date_field': 'start_datetime',
}

sitemaps = {
    'static': StaticViewSitemap,
    'flatpages': FlatPageSitemap,

    'news': GenericSitemap(news_dict, priority=0.6),
    'race': GenericSitemap(race_dict, priority=0.6),
    'blog': GenericSitemap(blog_dict, priority=0.6),
}

router = DefaultRouter()

router.register(r'photos', PhotoViewSet)
router.register(r'random_photos', RandomPhotoViewSet)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^404/$', TemplateView.as_view(template_name='404.html')),
    url(r'^500/$', TemplateView.as_view(template_name='500.html')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', 'members.views.officer_list', name='contact'),
    url(r'^contact/thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'^styleguide/$', StyleGuideView.as_view(), name='styleguide'),

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
    url(r'^comments/', include('django_comments.urls')),
    url(r'^djrill/', include('djrill.urls')),
    url(r'^api/v1/', include(router.urls)),

    url(r'^humans\.txt$', HumansView.as_view()),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^', include('favicon.urls')),

    # website templates
    url(r'^r/$', TemplateView.as_view(template_name='race_websites/index.html'), name='race_home'),
    url(r'^r/course/$', TemplateView.as_view(template_name='race_websites/course.html'), name='race_course'),
    url(r'^r/faqs/$', TemplateView.as_view(template_name='race_websites/faqs.html'), name='race_faqs'),
    url(r'^r/gallery/$', TemplateView.as_view(template_name='race_websites/gallery.html'), name='race_gallery'),
    url(r'^r/results/$', TemplateView.as_view(template_name='race_websites/results.html'), name='race_results'),
    url(r'^r/signup/$', TemplateView.as_view(template_name='race_websites/signup.html'), name='race_signup'),
    url(r'^r/travel/$', TemplateView.as_view(template_name='race_websites/travel.html'), name='race_travel'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('shorturls.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
