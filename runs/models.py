from django.db import models
from django.utils.translation import ugettext_lazy as _
from shorturls.models import ShortUrlMixin

from .managers import RunManager
from core.models import MachineTagMixin
from locations.models import Location
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
    location = models.ForeignKey(Location, blank=True, null=True)
    details = models.TextField()
    contact = models.ForeignKey(Member)
    active = models.BooleanField(default=True)

    objects = RunManager()

    class Meta:
        verbose_name = _('Run')
        verbose_name_plural = _('Runs')
        ordering = ['day_of_week']

    def __unicode__(self):
        return '{0}: {1}'.format(self.get_day_of_week_display(), self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('run_detail', (), {'slug': self.slug})
