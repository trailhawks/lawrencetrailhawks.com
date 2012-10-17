from django.db import models
from django.utils.translation import ugettext_lazy as _


class DraftManager(models.Manager):

    def get_query_set(self):
        queryset = super(DraftManager, self).get_query_set().filter(status__exact=HawkNews.STATUS_DRAFT)
        return queryset


class PublicManager(models.Manager):

    def get_query_set(self):
        queryset = super(PublicManager, self).get_query_set().filter(status__exact=HawkNews.STATUS_PUBLIC)
        return queryset


class HawkNews(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_PUBLIC)

    objects = models.Manager()
    published_objects = PublicManager()
    draft_objects = DraftManager()

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = _('hawk news')
        verbose_name_plural = _('hawk news')

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
            'year': self.start_datetime.strftime("%Y"),
            'month': self.start_datetime.strftime("%b").lower(),
            'day': self.start_datetime.strftime("%d"),
            'slug': self.slug})
