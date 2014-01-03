from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _


#class SocialWebsite(models.Model):
#    title = models.CharField(max_length=250)
#    slug = models.SlugField(blank=True, null=True)


# TODO: rename to remote status update?
class SocialLink(models.Model):
    """Represents a remote status update."""
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    message = models.TextField()
    remote_url = models.URLField(max_length=512, blank=True, null=True, help_text='Remote URL to status update')
    remote_id = models.CharField(max_length=128, blank=True, null=True, help_text='Remote ID of the status update')

    class Meta:
        #ordering = ('name',)
        verbose_name = _('Social Link')
        verbose_name_plural = _('Social Links')

    def __unicode__(self):
        return self.message

    #@models.permalink
    #def get_absolute_url(self):
    #    return ('link_detail', (), {'pk': self.pk})
