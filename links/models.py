from __future__ import unicode_literals
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from core.models import ShortUrlMixin


@python_2_unicode_compatible
class Links(models.Model, ShortUrlMixin):
    name = models.CharField(max_length=250)
    link = models.URLField(help_text='URL to link')
    description = models.TextField()

    content_type = models.ForeignKey('contenttypes.ContentType', blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ('name',)
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __str__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('link_detail', (), {'pk': self.pk})
