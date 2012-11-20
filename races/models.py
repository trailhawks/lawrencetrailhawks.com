import datetime

from django.db import models
from django.template.defaultfilters import slugify

from core.models import MachineTagMixin
from members.models import Member
from sponsors.models import Sponsor


class RaceType(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(RaceType, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Race(MachineTagMixin):
    KM = 1
    MI = 2
    UNIT_CHOICES = (
        (KM, "km"),
        (MI, "mi"),
    )
    RUN = 1
    BIKE = 2
    SWIM = 3
    DISCIPLINE_CHOICES = (
        (RUN, "Run"),
        (BIKE, "Bike"),
        (SWIM, "Swim"),
    )
    logo = models.ImageField(upload_to="races/logos", blank=True, null=True)
    slogan = models.CharField(max_length=300, blank=True, null=True)
    title = models.CharField(max_length=200, help_text="Title of event. If there are multiple races assoiated to an 'event', make two events.")
    annual = models.CharField(max_length=15)
    slug = models.SlugField(unique=True, help_text="Suggested value automatically generated from title and annual. Must be unique.")
    race_type = models.IntegerField(choices=DISCIPLINE_CHOICES, default=RUN)
    sponsors = models.ManyToManyField(Sponsor, related_name='sponsors')
    awards = models.CharField(max_length=300)
    distance = models.CharField(max_length=100, help_text="eg 26.2")
    unit = models.IntegerField(choices=UNIT_CHOICES, default=KM)
    start_datetime = models.DateTimeField(verbose_name="Start Date and Time")
    description = models.TextField()
    course_map = models.URLField(blank=True, null=True, verify_exists=False, help_text="Link to course map if avail.")
    cut_off = models.CharField(max_length=75, null=True, blank=True, help_text="eg: 13 hours")
    contact = models.ForeignKey(Member)
    location = models.TextField()
    location_iframe = models.TextField(blank=True, null=True)
    map_link = models.URLField(blank=True, null=True, verify_exists=False, help_text="Link to google maps or other mapping software pointing towards the start location")
    reg_url = models.URLField(blank=True, null=True, verify_exists=False, help_text="Link to registartion flyer or to registration URL for online signup.")
    reg_description = models.TextField()
    entry_form = models.FileField(upload_to="races/entry_forms", null=True, blank=True)
    discounts = models.TextField(blank=True, null=True, help_text="Describe discounts for the race if they exist.")
    lodging = models.URLField(blank=True, null=True, verify_exists=False, help_text="link to lodging information.")
    packet_pickup = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return u'{0} {1}'.format(self.annual, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('race_detail', (), {
            'year': self.start_datetime.strftime("%Y"),
            'month': self.start_datetime.strftime("%b").lower(),
            'day': self.start_datetime.strftime("%d"),
            'slug': self.slug})

    @property
    def get_overall_results(self):
        return self.result_set.all().order_by('race_type', 'time')

    @property
    def get_male_results(self):
        return self.result_set.filter(racer__gender=1).order_by('time')

    @property
    def get_female_results(self):
        return self.result_set.filter(racer__gender=2).order_by('time')

    @property
    def get_race_reports(self):
        return self.report_set.all()

    @property
    def get_reg_dates(self):
        return self.registration_set.all().order_by('reg_date')

    @property
    def get_race_type_results(self):
        return self.result_set.values_list('race_type__name', flat=True).distinct()

    @property
    def is_finished(self):
        if self.result_set.count == 0:
            return False
        else:
            return True


class Registration(models.Model):
    reg_date = models.DateField(verbose_name="Registration Date")
    reg_cost = models.IntegerField(verbose_name="Registration Cost")
    race = models.ForeignKey(Race)

    class Meta:
        verbose_name_plural = "Registration Dates"

    def __unicode__(self):
        return "%s %s" % (self.race.title, self.reg_date)


class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    relationship = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Racer(MachineTagMixin):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, "Male"),
        (FEMALE, "Female"),
    )

    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    XLARGE = 4
    SIZE_CHOICES = (
        (SMALL, "S"),
        (MEDIUM, "M"),
        (LARGE, "L"),
        (XLARGE, "XL"),
    )

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    trailhawk = models.ForeignKey(Member, unique=True, null=True, blank=True, help_text="If racer is a trailhawk select profile.")
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=13, blank=True, null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    shirt_size = models.IntegerField(choices=SIZE_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    contact = models.ForeignKey(EmergencyContact, verbose_name="Emergency Contact", blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        return ('racer_detail', (), {'object_id': self.pk})

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
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def get_results(self):
        return Result.objects.filter(racer=self)

    @property
    def age(self):
        TODAY = datetime.date.today()
        return (TODAY.year - self.birth_date.year)

    @property
    def get_gender(self):
        for num, gender in self.GENDER_CHOICES:
            if num == self.gender:
                return gender


class Result(models.Model):
    racer = models.ForeignKey(Racer)
    race = models.ForeignKey(Race)
    race_type = models.ForeignKey(RaceType, null=True, blank=True, help_text='For races with multiple race types.')
    bib_number = models.IntegerField()
    time = models.CharField(max_length=20, null=True, blank=True)
    place = models.TextField(null=True, blank=True, help_text='Ex. First Overall Male or First Masters Female')
    course_record = models.BooleanField()
    dq = models.BooleanField(verbose_name="Disqualified")
    dns = models.BooleanField(verbose_name="Did not Start")
    dnf = models.BooleanField(verbose_name="Did not Finish")

    def __unicode__(self):
        return "%s - %s - %s" % (self.racer, self.race.title, self.time)


class Report(models.Model):
    report = models.URLField(verify_exists=False, help_text="Link to race report")
    title = models.CharField(max_length=200)
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)

    def __unicode__(self):
        return self.title
