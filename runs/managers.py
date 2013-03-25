import datetime

from django.db.models import Manager
from django.db.models.query import QuerySet
from django.utils import timezone


class RunQuerySet(QuerySet):
    def today(self):
        weekday = timezone.now().weekday()
        return self.filter(active__exact=True, day_of_week=weekday)

    def next(self):
        for day in range(1, 6):
            weekday = (timezone.now() + datetime.timedelta(days=day)).weekday()
            next_day = self.filter(active__exact=True, day_of_week=weekday)
            if next_day.count():
                return next_day

        return []


class RunManager(Manager):
    def get_query_set(self):
        return RunQuerySet(self.model, using=self._db)

    def today(self):
        return self.get_query_set().today()

    def next(self):
        return self.get_query_set().next()
