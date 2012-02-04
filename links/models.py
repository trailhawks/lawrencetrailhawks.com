from __future__ import absolute_import

from django.db import models


class Links(models.Model):
    name = models.CharField(max_length=250)
    link = models.URLField(default="http://", help_text="URL to link")
    description = models.TextField()

    class Meta:
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __unicode__(self):
        return self.name
