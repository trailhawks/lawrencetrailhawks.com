from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from core.models import ShortUrlMixin


@python_2_unicode_compatible
class Location(models.Model, ShortUrlMixin):
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    zoom = models.IntegerField(null=True, blank=True, default='15')

    class Meta:
        ordering = ('name',)
        verbose_name = _('Location')
        verbose_name_plural = _('Location')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Location, self).save(*args, **kwargs)
