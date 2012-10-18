import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

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


class Run(models.Model):
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
    map_link = models.URLField(default="http://", help_text="Link to google maps location")
    details = models.TextField()
    contact = models.ForeignKey(Member)

    objects = models.Manager()
    today_objects = TodayManager()
    next_objects = NextManager()

    class Meta:
        verbose_name_plural = "Runs"
        ordering = ['day_of_week']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('lawrencetrailhawks.runs.views.run_detail', (), {'slug': self.slug})

    @property
    def get_run_news(self):
        return News.recent_objects.filter(run=self).order_by('-pub_date')


class DraftManager(models.Manager):

    def get_query_set(self):
        queryset = super(DraftManager, self).get_query_set().filter(status__exact=News.STATUS_DRAFT)
        return queryset


class PublicManager(models.Manager):

    def get_query_set(self):
        queryset = super(PublicManager, self).get_query_set().filter(status__exact=News.STATUS_PUBLIC)
        return queryset


class RecentManager(models.Manager):

    def get_query_set(self):
        recent_date = datetime.datetime.now() - datetime.timedelta(days=7)
        queryset = super(RecentManager, self).get_query_set().filter(status__exact=News.STATUS_PUBLIC, pub_date__gte=recent_date)
        return queryset


class News(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    run = models.ForeignKey(Run)
    body = models.TextField()
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_PUBLIC)

    objects = models.Manager()
    published_objects = PublicManager()
    draft_objects = DraftManager()
    recent_objects = RecentManager()

    class Meta:
        verbose_name_plural = "Latest Run Updates"

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {'year': self.start_datetime.strftime("%Y"),
                                    'month': self.start_datetime.strftime("%b").lower(),
                                    'day': self.start_datetime.strftime("%d"),
                                    'slug': self.slug})
