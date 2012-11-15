from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('faq_detail', (), {'object_id': self.pk})
