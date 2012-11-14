import logging

from django.core.management.base import BaseCommand

from news.models import News
from hawknews.models import HawkNews
from races.models import News as RaceNews
from runs.models import News as RunNews


class Command(BaseCommand):

    def get_or_create_news(self, title, slug, pub_date, body, status, obj=None):
        defaults = {
            'title': title,
            'body': body,
            'status': status,
        }

        if obj:
            defaults['content_object'] = obj

        news, created = News.objects.get_or_create(title=title, pub_date=pub_date, defaults=defaults)
        if created:
            self.log.debug('created news ({0})'.format(news.pk))

    def import_hawknew(self):
        for obj in HawkNews.objects.all():
            self.log.debug('importing hawk news ({0})'.format(obj.pk))
            try:
                self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.status)
            except Exception as e:
                self.log.exception(e)

    def import_race_news(self):
        for obj in RaceNews.objects.all():
            self.log.debug('importing race news ({0})'.format(obj.pk))
            try:
                self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.draft, obj=obj.race)
            except Exception as e:
                self.log.exception(e)

    def import_run_news(self):
        for obj in RunNews.objects.all():
            self.log.debug('importing run news ({0})'.format(obj.pk))
            try:
                self.get_or_create_news(obj.title, obj.slug, obj.pub_date, obj.body, obj.status, obj.run)
            except Exception as e:
                self.log.exception(e)

    def handle(self, *args, **options):
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        self.log.addHandler(ch)

        self.import_hawknew()
        self.import_race_news()
        self.import_run_news()
