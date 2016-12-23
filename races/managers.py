from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils import timezone


class RaceQuerySet(QuerySet):

    def active(self):
        return self.filter(active__exact=True)

    def complete(self):
        return self.active().filter(start_datetime__lte=timezone.now())

    def upcoming(self):
        return self.active().filter(start_datetime__gt=timezone.now())


class RaceManager(Manager):

    def get_queryset(self):
        return RaceQuerySet(self.model, using=self._db)

    def complete(self):
        return self.get_queryset().complete()

    def upcoming(self):
        return self.get_queryset().upcoming()
