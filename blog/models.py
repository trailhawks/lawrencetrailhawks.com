from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_comments.moderation import CommentModerator, moderator
from taggit.managers import TaggableManager

# from . import listeners
from .managers import PostManager
from core.models import CommentMixin, ShortUrlMixin


@python_2_unicode_compatible
class Post(CommentMixin, ShortUrlMixin, models.Model):
    """Post model."""

    STATUS_DRAFT = 1
    STATUS_PUBLIC = 2
    STATUS_CHOICES = (
        (STATUS_DRAFT, _('Draft')),
        (STATUS_PUBLIC, _('Public')),
    )
    title = models.CharField(_('title'), max_length=200)
    slug = models.SlugField(_('slug'), unique_for_date='publish')
    author = models.ForeignKey('members.Member', blank=True, null=True)
    body = models.TextField(_('body'), help_text="The body supports Textile markup. Please use http://textile.thresholdstate.com/ to markup the blog post and get the right formatting.")
    tease = models.TextField(_('tease'), blank=True, help_text=_('Concise text suggested. Does not appear in RSS feed.'))
    status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=STATUS_PUBLIC)
    publish = models.DateTimeField(_('publish'), default=timezone.now)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    repost_url = models.URLField(help_text="URL of original blog posting.",
                                 verbose_name='Original Post', null=True, blank=True)
    repost_date = models.DateField(help_text="Date of original blog posting",
                                   verbose_name="Original Post Date", null=True, blank=True)

    tags = TaggableManager(blank=True)
    objects = PostManager()

    class Meta:
        db_table = 'blog_posts'
        get_latest_by = 'publish'
        ordering = ('-publish',)
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('blog_detail', None, {
            'year': self.publish.year,
            'month': self.publish.strftime('%b').lower(),
            'day': self.publish.strftime('%d'),
            'slug': self.slug
        })

    def get_previous_post(self):
        return self.get_previous_by_publish(status__gte=self.STATUS_PUBLIC)

    def get_next_post(self):
        return self.get_next_by_publish(status__gte=self.STATUS_PUBLIC)


class PostModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
    auto_close_field = 'publish'
    close_after = 7


moderator.register(Post, PostModerator)
