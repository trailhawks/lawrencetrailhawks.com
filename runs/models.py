import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from shorturls.models import ShortUrlMixin

from core.models import MachineTagMixin
from members.models import Member


class TodayManager(models.Manager):

    def get_query_set(self):
        weekday = datetime.datetime.now().weekday()
        queryset = super(TodayManager, self).get_query_set().filter(day_of_week=weekday)
        return queryset


class NextManager(models.Manager):

    def get_query_set(self):
        queryset = super(NextManager, self).get_query_set()
        for day in range(1, 6):
            weekday = (datetime.datetime.now() + datetime.timedelta(days=day)).weekday()
            next_day = queryset.filter(day_of_week=weekday)
            if next_day.count():
                return next_day
        return []


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
    map_iframe = models.TextField(blank=True, null=True)
    map_link = models.URLField(blank=True, null=True, verify_exists=False, help_text="Link to google maps location")
    details = models.TextField()
    contact = models.ForeignKey(Member)
    active = models.BooleanField(default=True)

    objects = models.Manager()
    today_objects = TodayManager()
    next_objects = NextManager()

    class Meta:
        verbose_name = _('Run')
        verbose_name_plural = _('Runs')
        ordering = ['day_of_week']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('run_detail', (), {'slug': self.slug})
