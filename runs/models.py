from __future__ import absolute_import

from django.db import models

from members.models import Member


class Run(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")
    order = models.IntegerField(default=10)
    run_date = models.CharField(max_length=25,
                                help_text="Day of run (ex. Monday)")
    run_time = models.CharField(max_length=25,
                                help_text="Time of run (ex. 6:30 PM)")
    location = models.TextField()
    map_iframe = models.TextField(blank=True, null=True)
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps location")
    details = models.TextField()
    contact = models.ForeignKey(Member)

    class Meta:
        verbose_name_plural = "Runs"

    class Meta:
        ordering = ['order']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
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
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {'year': self.start_datetime.strftime("%Y"),
                                    'month': self.start_datetime.strftime("%b").lower(),
                                    'day': self.start_datetime.strftime("%d"),
                                    'slug': self.slug})
