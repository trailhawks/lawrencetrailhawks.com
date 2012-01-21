from django.db import models


class SponsorManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class Sponsor(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from name. Must be unique.")
    url = models.URLField(default="http://",
                          help_text="URL to website")
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField()
    logo = models.ImageField(upload_to="sponsors/images")
    discount_detail = models.TextField()
    active = models.BooleanField()

    objects = SponsorManager()

    class Meta:
        verbose_name_plural = "Sponsors"

    def __unicode__(self):
        return self.name
