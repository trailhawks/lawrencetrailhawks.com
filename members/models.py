import datetime

from django.contrib.auth.models import User
from django.db import models

from core.models import MachineTagMixin


class ActiveMemberManager(models.Manager):

    def get_query_set(self):
        queryset = super(ActiveMemberManager, self).get_query_set().filter(date_paid__lte=datetime.date.today())
        return queryset


class ReceiveCommentEmailsManager(models.Manager):

    def get_query_set(self):
        queryset = super(ReceiveCommentEmailsManager, self).get_query_set().filter(email__isnull=False, receive_comment_emails__exact=True)
        return queryset


class Member(MachineTagMixin):
    PRESIDENT = 1
    VICE_PRESIDENT = 2
    TREASURER = 3
    SECRETARY = 4
    WEB_MASTER = 5
    MEMBERSHIP_DIRECTOR = 6
    PR = 7
    EX_PRESIDENT = 8
    SOCIAL_MEDIA_DIRECTOR = 9

    POSITION_CHOICES = (
        (PRESIDENT, 'President'),
        (VICE_PRESIDENT, 'Vice President'),
        (TREASURER, 'Treasurer'),
        (SECRETARY, 'Secretary'),
        (WEB_MASTER, 'Web Master'),
        (MEMBERSHIP_DIRECTOR, 'Membership Director'),
        (PR, 'PR Director'),
        (EX_PRESIDENT, 'Ex-President'),
        (SOCIAL_MEDIA_DIRECTOR, 'Social Media Director'),
    )

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
    avatar = models.ImageField(upload_to='members/avatars', blank=True, null=True)
    #active = models.BooleanField()
    date_paid = models.DateField(null=True, blank=True)
    member_since = models.DateField(null=True, blank=True)
    position = models.IntegerField(choices=POSITION_CHOICES, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    receive_comment_emails = models.BooleanField(default=False, help_text='Should this member be notified when a comment is left on the website?')

    objects = models.Manager()
    active_objects = ActiveMemberManager()
    comment_email_objects = ReceiveCommentEmailsManager()

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ['last_name']

    def __unicode__(self):
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
    def position_name(self):
        if self.position:
            return dict(Member.POSITION_CHOICES)[self.position]

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
        return Result.objects.filter(racer__trailhawk=self)

    @property
    def get_race_reports(self):
        from races.models import Report
        return Report.objects.filter(racer__trailhawk=self)
