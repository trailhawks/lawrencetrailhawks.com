from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class SponsorManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, null=True, help_text='Suggested value automatically generated from name. Must be unique.')
    url = models.URLField(verify_exists=False, help_text='URL to website')
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to='sponsors/images')
    discount_detail = models.TextField()
    active = models.BooleanField()

    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = SponsorManager()

    class Meta:
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Sponsor, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('sponsor_detail', (), {'pk': self.pk})
