from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'homepage',
            'calendar',
            'contact',
            'course',
            'faqs',
            'gallery',
            'results',
            'signup',
            'travel',
        ]

    def location(self, item):
        return reverse(item)
