import datetime

from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils import timezone


class NewsQuerySet(QuerySet):

    def draft(self):
        return self.filter(status__exact=self.model.STATUS_DRAFT)

    def public(self):
        return self.filter(status__exact=self.model.STATUS_PUBLIC)

    def recent(self):
        recently = timezone.now() - datetime.timedelta(days=14)
        return self.filter(pub_date__gte=recently)


class NewsManager(Manager):

    def get_queryset(self):
        return NewsQuerySet(self.model, using=self._db)

    def draft(self):
        return self.get_queryset().draft()

    def public(self):
        return self.get_queryset().public()

    def recent(self):
        return self.get_queryset().recent()
