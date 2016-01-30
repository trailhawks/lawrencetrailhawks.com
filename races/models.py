from __future__ import unicode_literals

from ajaximage.fields import AjaxImageField
from django.db import models
from django.template.defaultfilters import slugify, title
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django_comments.moderation import CommentModerator, moderator
from num2words import num2words

from .managers import RaceManager
from core.models import CommentMixin, MachineTagMixin, ShortUrlMixin


@python_2_unicode_compatible
class RaceType(models.Model):
    """Race Type model."""

    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(RaceType, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Race(MachineTagMixin, CommentMixin, ShortUrlMixin):
    """Race model."""

    KM = 1
    MI = 2
    UNIT_CHOICES = (
        (KM, _('Kilometers')),
        (MI, _('Miles')),
    )
    RUN = 1
    BIKE = 2
    SWIM = 3
    DISCIPLINE_CHOICES = (
        (RUN, _('Run')),
        (BIKE, _('Bike')),
        (SWIM, _('Swim')),
    )
    title = models.CharField(max_length=200,
                             help_text='Title of event. If there are multiple races assoiated to an "event", make two events.')
    active = models.BooleanField(default=True)
    number = models.IntegerField(blank=True, null=True)
    annual = models.CharField(max_length=15, blank=True, null=True)
    slug = models.SlugField(unique=True,
                            help_text='Suggested value automatically generated from title and annual. Must be unique.')

    slogan = models.CharField(max_length=300, blank=True, null=True)

    logo = AjaxImageField(upload_to='races/logos', blank=True, null=True)

    # background = AjaxImageField(upload_to='races/backgrounds', blank=True, null=True,
    #                             help_text='Optional background photo')
    background = models.ForeignKey('flickr.Photo', blank=True, null=True)

    race_type = models.IntegerField(choices=DISCIPLINE_CHOICES, default=RUN)
    sponsors = models.ManyToManyField('sponsors.Sponsor', related_name='sponsors')
    race_directors = models.ManyToManyField('members.Member')
    awards = models.TextField(blank=True, null=True)
    distance = models.CharField(max_length=100, blank=True, null=True,
                                help_text='eg 26.2')
    unit = models.IntegerField(choices=UNIT_CHOICES, default=KM, blank=True, null=True)
    start_datetime = models.DateTimeField(verbose_name='Start Date and Time')
    description = models.TextField()
    location = models.ForeignKey('locations.Location', blank=True, null=True)
    course_map = models.URLField(blank=True, null=True,
                                 help_text='Link to course map if avail.')
    cut_off = models.CharField(max_length=75, null=True, blank=True,
                               help_text='eg: 13 hours')
    reg_url = models.URLField(blank=True, null=True,
                              help_text='Link to registartion flyer or to registration URL for online signup.')
    reg_description = models.TextField(blank=True, null=True)
    entry_form = models.FileField(upload_to='races/entry_forms', null=True, blank=True)
    discounts = models.TextField(blank=True, null=True,
                                 help_text='Describe discounts for the race if they exist.')
    lodging = models.URLField(blank=True, null=True,
                              help_text='Link to lodging information')
    packet_pickup = models.TextField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True,
                                   help_text='Link to Facebook page')
    facebook_event_url = models.URLField(blank=True, null=True,
                                         help_text='Link to Facebook Event page')

    objects = RaceManager()

    class Meta:
        ordering = ['-start_datetime']
        verbose_name = _('Race')
        verbose_name_plural = _('Races')

    def __str__(self):
        return self.get_full_name()

    @models.permalink
    def get_absolute_url(self):
        return ('race_detail', (), {
            'year': self.start_datetime.strftime('%Y'),
            'month': self.start_datetime.strftime('%b').lower(),
            'day': self.start_datetime.strftime('%d'),
            'slug': self.slug})

    def get_full_name(self):
        name = ''
        if self.number:
            number = num2words(self.number, ordinal=True)
            if self.number == 1:
                name = 'Inaugural {0}'.format(self.title)
            else:
                name = '{0} Annual {1}'.format(number, self.title)
        else:
            name = '{0} {1}'.format(self.annual, self.title)
        return title(name)

    @cached_property
    def ical_uid(self):
        return 'race-{0}@trailhawks.com'.format(self.pk)

    @cached_property
    def get_overall_results(self):
        return self.result_set.all().order_by('race_type', 'time')

    @cached_property
    def get_race_reports(self):
        return self.report_set.all()

    @cached_property
    def is_finished(self):
        return not self.result_set.count() == 0


class RaceModerator(CommentModerator):
    email_notification = True
    enable_field = 'enable_comments'
    auto_close_field = 'start_datetime'
    close_after = 30


moderator.register(Race, RaceModerator)


@python_2_unicode_compatible
class Registration(models.Model):
    """Registration model."""

    race = models.ForeignKey('races.Race')
    description = models.CharField(max_length=100, blank=True, null=True)
    reg_date = models.DateField('Registration Date')
    end_date = models.DateField('End Date', blank=True, null=True)
    reg_cost = models.IntegerField('Registration Cost')

    class Meta:
        verbose_name = _('Registration Dates')
        verbose_name_plural = _('Registration Dates')

    def __str__(self):
        return '%s %s' % (self.race.title, self.reg_date)

    @property
    def has_expired(self):
        if self.end_date:
            return timezone.now() < self.end_date
        return False


@python_2_unicode_compatible
class EmergencyContact(models.Model):
    """Emergency Contact model."""

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    relationship = models.CharField(max_length=40)

    class Meta:
        verbose_name = _('Emergency Contact')
        verbose_name_plural = _('Emergency Contacts')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


@python_2_unicode_compatible
class Racer(MachineTagMixin):
    """Racer model."""

    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XLARGE = 4
    SIZE_CHOICES = (
        (SMALL, 'S'),
        (MEDIUM, 'M'),
        (LARGE, 'L'),
        (XLARGE, 'XL'),
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    trailhawk = models.ForeignKey('members.Member', unique=True, null=True, blank=True,
                                  help_text='If racer is a trailhawk select profile.')
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    shirt_size = models.IntegerField(choices=SIZE_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    contact = models.ForeignKey('races.EmergencyContact', verbose_name='Emergency Contact', blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = _('Racer')
        verbose_name_plural = _('Racers')

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('racer_detail', (), {'pk': self.pk})

    def get_machine_tags(self):
        machine_tags = super(Racer, self).get_machine_tags()
        try:
            if self.trailhawk:
                machine_tags += self.trailhawk.get_machine_tags()
        except IndexError:
            pass
        return machine_tags

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @property
    def get_results(self):
        return Result.objects.filter(racer=self)

    @property
    def age(self):
        TODAY = timezone.today()
        return (TODAY.year - self.birth_date.year)

    @property
    def get_gender(self):
        for num, gender in self.GENDER_CHOICES:
            if num == self.gender:
                return gender


@python_2_unicode_compatible
class Result(models.Model):
    """Result model."""

    racer = models.ForeignKey('races.Racer')
    race = models.ForeignKey('races.Race')
    race_type = models.ForeignKey('races.RaceType', null=True, blank=True,
                                  help_text='For races with multiple race types.')
    bib_number = models.IntegerField()
    time = models.CharField(max_length=20, null=True, blank=True)
    place = models.TextField(null=True, blank=True,
                             help_text='Ex. First Overall Male or First Masters Female')
    course_record = models.BooleanField(default=False)
    dq = models.BooleanField('Disqualified', default=False)
    dns = models.BooleanField('Did not Start', default=False)
    dnf = models.BooleanField('Did not Finish', default=False)

    class Meta:
        ordering = ('time',)
        verbose_name = _('Result')
        verbose_name_plural = _('Results')

    def __str__(self):
        return '%s - %s - %s' % (self.racer, self.race.title, self.time)

    def save(self, *args, **kwargs):

        if 'cr' in self.time.lower():
            self.course_record = True

        if 'dnf' in self.time.lower():
            self.dnf = True

        if 'dns' in self.time.lower():
            self.dns = True

        return super(Result, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Report(models.Model):
    """Report model."""

    report = models.URLField(help_text='Link to race report')
    title = models.CharField(max_length=200)
    race = models.ForeignKey('races.Race')
    racer = models.ForeignKey('races.Racer')

    class Meta:
        verbose_name = _('Report')
        verbose_name_plural = _('Reports')

    def __str__(self):
        return self.title
