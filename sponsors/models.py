from __future__ import unicode_literals

from ajaximage.fields import AjaxImageField
from django.contrib.contenttypes import generic
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .managers import SponsorManager


@python_2_unicode_compatible
class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True, help_text='Suggested value automatically generated from name. Must be unique.')
    url = models.URLField(help_text='URL to website')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    logo = AjaxImageField(upload_to='sponsors', blank=True, null=True)
    discount_detail = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=False)
    homepage = models.BooleanField('Show on homepage?', default=False)

    content_type = models.ForeignKey('contenttypes.ContentType', blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = SponsorManager()

    class Meta:
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Sponsor, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('sponsor_detail', (), {'pk': self.pk})
