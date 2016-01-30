from __future__ import unicode_literals
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_comments.moderation import CommentModerator, moderator

from core.models import CommentMixin, MachineTagMixin, ShortUrlMixin
from .managers import EventManager


@python_2_unicode_compatible
class Event(MachineTagMixin, CommentMixin, ShortUrlMixin):
    """Event model."""

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
    facebook_url = models.URLField(blank=True, null=True, help_text='Link to Facebook page')
    facebook_event_url = models.URLField(blank=True, null=True, help_text='Link to Facebook Event page')
    races = models.ManyToManyField('races.Race', related_name='events')

    objects = EventManager()

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
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


class EventModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
    # auto_close_field = 'publish'
    # close_after = 7


moderator.register(Event, EventModerator)
