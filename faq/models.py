from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')

    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return ('faq_detail', (), {'pk': self.pk})
