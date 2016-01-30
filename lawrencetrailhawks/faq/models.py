from __future__ import unicode_literals
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from core.models import ShortUrlMixin


@python_2_unicode_compatible
class FAQ(models.Model, ShortUrlMixin):
    question = models.TextField()
    answer = models.TextField()

    content_type = models.ForeignKey('contenttypes.ContentType', blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('-content_type',)
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __str__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return ('faq_detail', (), {'pk': self.pk})
