from __future__ import unicode_literals

import datetime

from ajaximage.fields import AjaxImageField
from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from core.models import MachineTagMixin, ShortUrlMixin
from .managers import MemberManager, TermManager


@python_2_unicode_compatible
class Member(MachineTagMixin, ShortUrlMixin):
    GENDER_CHOICES = (
        (1, 'Male'),
        (2, 'Female'),
    )

    username = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hawk_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    address2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    zip = models.CharField(max_length=25, blank=True, null=True)
    avatar = AjaxImageField(upload_to='members/avatars', blank=True, null=True)
    date_paid = models.DateField(null=True, blank=True)
    member_since = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    receive_comment_emails = models.BooleanField(default=False, help_text='Should this member be notified when a comment is left on the website?')

    objects = MemberManager()

    class Meta:
        verbose_name = _('Member')
        verbose_name_plural = _('Members')
        ordering = ['last_name']

    def __str__(self):
        return self.full_hawk_name

    @models.permalink
    def get_absolute_url(self):
        return ('member_detail', (), {'pk': self.pk})

    def get_machine_tags(self):
        machine_tags = super(Member, self).get_machine_tags()
        machine_tags += [
            'trailhawk:member={0}'.format('-'.join([self.first_name, self.last_name]).lower())
        ]
        return machine_tags

    def active(self):
        try:
            return self.date_expires >= datetime.date.today()
        except:
            return False
    active.boolean = True

    @property
    def date_expires(self):
        date_expires = self.date_paid + datetime.timedelta(weeks=52)
        return date_expires

    @property
    def full_hawk_name(self):
        if self.hawk_name:
            return '%s "%s" %s' % (self.first_name, self.hawk_name, self.last_name)
        else:
            return '%s %s' % (self.first_name, self.last_name)

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def get_position(self):
        for pos, title in self.POSITION_CHOICES:
            if self.position == pos:
                return title

    @property
    def get_blog_posts(self):
        from blog.models import Post
        return Post.objects.filter(author=self)

    @property
    def get_race_results(self):
        from races.models import Result
        return Result.objects.filter(racer__trailhawk=self).order_by('-race__start_datetime')

    @property
    def get_race_reports(self):
        from races.models import Report
        return Report.objects.filter(racer__trailhawk=self)


@python_2_unicode_compatible
class Office(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    order = models.IntegerField(default=100)

    class Meta:
        verbose_name = 'office'
        verbose_name_plural = 'offices'

    def __str__(self):
        return self.name


class Term(models.Model):
    office = models.ForeignKey(Office, blank=True, null=True)
    member = models.ForeignKey(Member, blank=True, null=True)
    start = models.DateField()
    end = models.DateField(blank=True, null=True)

    objects = TermManager()

    class Meta:
        verbose_name = 'term'
        verbose_name_plural = 'terms'
