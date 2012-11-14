from datetime import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class DraftManager(models.Manager):

    def get_query_set(self):
        queryset = super(DraftManager, self).get_query_set().filter(status__exact=News.STATUS_DRAFT)
        return queryset


class PublicManager(models.Manager):

    def get_query_set(self):
        queryset = super(PublicManager, self).get_query_set().filter(status__exact=News.STATUS_PUBLIC)
        return queryset


class News(models.Model):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    pub_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_PUBLIC)

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = models.Manager()
    published_objects = PublicManager()
    draft_objects = DraftManager()

    class Meta:
        ordering = ('-pub_date',)
        unique_together = (('slug', 'pub_date'),)
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        #now = timezone.now()
        now = datetime.now()
        self.updated = now

        if not self.pub_date and self.status == self.STATUS_PUBLIC:
            self.pub_date = now

        super(News, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {
            'year': self.start_datetime.strftime("%Y"),
            'month': self.start_datetime.strftime("%b").lower(),
            'day': self.start_datetime.strftime("%d"),
            'slug': self.slug})
