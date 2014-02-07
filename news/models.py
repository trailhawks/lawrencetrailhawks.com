from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from shorturls.models import ShortUrlMixin

from .managers import NewsManager


ALERT_CHOICES = (
    ('', _('Default no style.')),
    ('success', _('success')),
    ('info', _('info')),
    ('warning', _('warning')),
    ('danger', _('danger')),
)


class News(models.Model, ShortUrlMixin):
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
    alert_status = models.CharField(max_length=50, choices=ALERT_CHOICES, default='')

    # show in main news feed? handy for race results...
    content_type = models.ForeignKey(ContentType, blank=True, null=True)
    object_id = models.PositiveIntegerField(blank=True, null=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    objects = NewsManager()

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

        now = timezone.now()

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
