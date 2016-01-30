from __future__ import unicode_literals
from django.contrib.contenttypes import generic
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


# class SocialWebsite(models.Model):
#    title = models.CharField(max_length=250)
#    slug = models.SlugField(blank=True, null=True)


# TODO: rename to remote status update?
@python_2_unicode_compatible
class SocialLink(models.Model):
    """Represents a remote status update."""
    content_type = models.ForeignKey('contenttypes.ContentType')
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    message = models.TextField()
    remote_url = models.URLField(max_length=512, blank=True, null=True, help_text='Remote URL to status update')
    remote_id = models.CharField(max_length=128, blank=True, null=True, help_text='Remote ID of the status update')

    class Meta:
        verbose_name = _('Social Link')
        verbose_name_plural = _('Social Links')

    def __str__(self):
        return self.message

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('link_detail', (), {'pk': self.pk})
