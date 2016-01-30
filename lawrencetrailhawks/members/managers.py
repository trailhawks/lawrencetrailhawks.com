import datetime

from django.db.models import Manager, Q
from django.db.models.query import QuerySet
from django.utils import timezone


class MemberQuerySet(QuerySet):

    def current(self):
        one_year_ago = timezone.now() - datetime.timedelta(weeks=52)
        return self.filter(date_paid__gte=one_year_ago)

    def previous(self):
        one_year_ago = timezone.now() - datetime.timedelta(weeks=52)
        return self.filter(date_paid__lt=one_year_ago)

    def receive_comment_emails(self):
        return self.filter(email__isnull=False, receive_comment_emails__exact=True)


class MemberManager(Manager):

    def get_query_set(self):
        return MemberQuerySet(self.model, using=self._db)

    def current(self):
        return self.get_query_set().current()

    def previous(self):
        return self.get_query_set().previous()

    def receive_comment_emails(self):
        return self.get_query_set().receive_comment_emails()


class TermQuerySet(QuerySet):

    def current(self):
        query = Q(start__lte=timezone.now()) & Q(end=None) | Q(end__gt=timezone.now())
        return self.filter(query)  # .order_by('-start_datetime')

    def previous(self):
        query = Q(start__lt=timezone.now()) & Q(end__lt=timezone.now())
        return self.filter(query)  # .order_by('-start_datetime')


class TermManager(Manager):

    def get_query_set(self):
        return TermQuerySet(self.model, using=self._db)

    def current(self):
        return self.get_query_set().current()

    def previous(self):
        return self.get_query_set().previous()
