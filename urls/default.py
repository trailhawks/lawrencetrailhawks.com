from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from ..views import AboutView, HomepageView, StyleGuideView, ThanksView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomepageView.as_view(), name='homepage'),
    url(r'^404/', TemplateView.as_view(template_name='404.html')),
    url(r'^500/', TemplateView.as_view(template_name='500.html')),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^contact/$', 'members.views.officer_list', name='contact'),
    url(r'^contact/thanks/$', ThanksView.as_view(), name='thanks'),
    url(r'^member_list/$', 'members.views.member_list', name='member_list'),
    url(r'^styleguide/$', StyleGuideView.as_view(), name='styleguide'),
    url(r'^blog/', include('blog.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^faq/', include('faq.urls')),
    url(r'^links/', include('links.urls')),
    url(r'^members/', include('members.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^photos/', include('photos.urls')),
    url(r'^races/', include('races.urls')),
    url(r'^runs/', include('runs.urls')),
    url(r'^sponsors/', include('sponsors.urls')),
    url(r'^djrill/', include('djrill.urls')),
    url(r'^ajaximage/', include('ajaximage.urls')),

    # website templates
    url(r'^r/$', TemplateView.as_view(template_name='race_websites/index.html'), name='race_home'),
    url(r'^r/course/$', TemplateView.as_view(template_name='race_websites/course.html'), name='race_course'),
    url(r'^r/calendar/$', TemplateView.as_view(template_name='race_websites/calendar.html'), name='race_calendar'),
    url(r'^r/faqs/$', TemplateView.as_view(template_name='race_websites/faqs.html'), name='race_faqs'),
    url(r'^r/travel/$', TemplateView.as_view(template_name='race_websites/travel.html'), name='race_travel'),
    url(r'^r/gallery/$', TemplateView.as_view(template_name='race_websites/gallery.html'), name='race_gallery'),
    url(r'^r/results/$', TemplateView.as_view(template_name='race_websites/results.html'), name='race_results'),
    url(r'^r/signup/$', TemplateView.as_view(template_name='race_websites/signup.html'), name='race_signup'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('shorturls.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
