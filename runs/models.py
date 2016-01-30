from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_comments.moderation import CommentModerator, moderator

from .managers import RunManager
from core.models import CommentMixin, MachineTagMixin, ShortUrlMixin


@python_2_unicode_compatible
class Run(MachineTagMixin, CommentMixin, ShortUrlMixin):
    """Run model."""

    DAY_OF_WEEK = (
        (0, _('Monday')),
        (1, _('Tuesday')),
        (2, _('Wednesday')),
        (3, _('Thursday')),
        (4, _('Friday')),
        (5, _('Saturday')),
        (6, _('Sunday')),
    )
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title. Must be unique.")
    day_of_week = models.IntegerField(choices=DAY_OF_WEEK, default=0)
    run_time = models.CharField(max_length=25, help_text="Time of run (ex. 6:30 PM)")
    location = models.ForeignKey('locations.Location', blank=True, null=True)
    details = models.TextField()
    contact = models.ForeignKey('members.Member')
    active = models.BooleanField(default=True)

    objects = RunManager()

    class Meta:
        ordering = ['day_of_week']
        verbose_name = _('Run')
        verbose_name_plural = _('Runs')

    def __str__(self):
        return '{0}: {1}'.format(self.get_day_of_week_display(), self.name)

    @models.permalink
    def get_absolute_url(self):
        return ('run_detail', (), {'slug': self.slug})


class RunModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'


moderator.register(Run, RunModerator)
