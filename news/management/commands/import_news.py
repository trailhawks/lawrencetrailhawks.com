import logging

from django.core.management.base import BaseCommand

from news.models import News
from hawknews.models import HawkNews
from races.models import Race, News as RaceNews
from runs.models import Run, News as RunNews


class Command(BaseCommand):

    def get_or_create_news(self, title, slug, pub_date, body, status, obj=None):
        defaults = {
            'title': title,
            'body': body,
            'status': status,
        }

        # do something special
        if obj:
            defaults['content_object'] = obj

        news, created = News.objects.get_or_create(title=title, pub_date=pub_date, defaults=defaults)
        if created:
            self.log.debug('created news ({0})'.format(news.pk))
        #news.delete()

    def import_hawknew(self):
        for obj in HawkNews.objects.all():
            self.log.debug('importing hawk news ({0})'.format(obj.pk))
            self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.status)

    def import_race_news(self):
        for obj in RaceNews.objects.all():
            self.log.debug('importing race news ({0})'.format(obj.pk))
            #import ipdb
            #ipdb.set_trace()
            self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.status, obj=obj.race)

    def import_run_news(self):
        for obj in RunNews.objects.all():
            self.log.debug('importing run news ({0})'.format(obj.pk))
            #import ipdb
            #ipdb.set_trace()
            self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.status, obj.run)

    def handle(self, *args, **options):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.log.addHandler(ch)

        print News.objects.count()
        print HawkNews.objects.count()
        print RaceNews.objects.count()
        print RunNews.objects.count()

        self.import_hawknew()
        self.import_race_news()
        self.import_run_news()
