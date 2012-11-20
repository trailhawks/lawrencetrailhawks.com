from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Links(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(verify_exists=False, help_text='URL to link')
    description = models.TextField()

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('link_detail', (), {'pk': self.pk})
