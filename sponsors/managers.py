from django.db.models import Manager
from django.db.models.query import QuerySet


class SponsorQuerySet(QuerySet):

    def active(self):
        return self.filter(active__exact=True)

    def homepage(self):
        return self.active().filter(homepage__exact=True)


class SponsorManager(Manager):

    def get_queryset(self):
        return SponsorQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def homepage(self):
        return self.get_queryset().homepage()
