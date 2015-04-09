from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils import timezone


class RaceQuerySet(QuerySet):

    def complete(self):
        return self.filter(start_datetime__lte=timezone.now())

    def upcoming(self):
        return self.filter(start_datetime__gt=timezone.now())


class RaceManager(Manager):

    def get_query_set(self):
        return RaceQuerySet(self.model, using=self._db)

    def complete(self):
        return self.get_query_set().complete()

    def upcoming(self):
        return self.get_query_set().upcoming()
