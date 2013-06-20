from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from shorturls.models import ShortUrlMixin

from core.models import MachineTagMixin
from races.models import Race


class DraftManager(models.Manager):

    def get_query_set(self):
        queryset = super(DraftManager, self).get_query_set().filter(status__exact=Event.STATUS_DRAFT)
        return queryset


class PublicManager(models.Manager):

    def get_query_set(self):
        queryset = super(PublicManager, self).get_query_set().filter(status__exact=Event.STATUS_PUBLIC)
        return queryset


class Event(MachineTagMixin, ShortUrlMixin):
    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_PUBLIC)
    races = models.ManyToManyField(Race, related_name='events')
    #allow_comments = models.BooleanField(_('allow comments'), default=True)

    objects = models.Manager()
    published_objects = PublicManager()
    draft_objects = DraftManager()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        now = timezone.now()

        if self.status == self.STATUS_PUBLIC:
            self.pub_date = now

        super(Event, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', (), {'slug': self.slug})
