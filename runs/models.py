from django.db import models
from django.utils.translation import ugettext_lazy as _
from shorturls.models import ShortUrlMixin

from .managers import RunManager
from core.models import MachineTagMixin
from members.models import Member


class Run(MachineTagMixin, ShortUrlMixin):
    DAY_OF_WEEK = (
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK, default=0)
    run_time = models.CharField(max_length=25, help_text="Time of run (ex. 6:30 PM)")
    location = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, null=True, blank=True)
    map_iframe = models.TextField(blank=True, null=True)
    map_link = models.URLField(blank=True, null=True, help_text="Link to google maps location")
    details = models.TextField()
    contact = models.ForeignKey(Member)
    active = models.BooleanField(default=True)

    objects = RunManager()

    class Meta:
        verbose_name = _('Run')
        verbose_name_plural = _('Runs')
        ordering = ['day_of_week']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('run_detail', (), {'slug': self.slug})

    def is_geocoded(self):
        if self.latitude and self.longitude:
            return True
        else:
            return False
    is_geocoded.boolean = True
