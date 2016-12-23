from django.db.models import Manager
from django.db.models.query import QuerySet


class PostQuerySet(QuerySet):
    def draft(self):
        return self.filter(status__exact=self.model.STATUS_DRAFT)

    def public(self):
        return self.filter(status__exact=self.model.STATUS_PUBLIC)


class PostManager(Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def draft(self):
        return self.get_queryset().draft()

    def public(self):
        return self.get_queryset().public()
