from django.db import models

from lawrencetrailhawks.members.models import Member


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
        return News.objects.filter(run=self, draft=2).order_by('-pub_date')


class News(models.Model):
    DRAFT = 1
    PUBLIC = 2
    DRAFT_CHOICES = (
        (DRAFT, "Draft",),
        (PUBLIC, "Public",),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    run = models.ForeignKey(Run)
    body = models.TextField()
    draft = models.IntegerField(choices=DRAFT_CHOICES)

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
