import datetime

from django.db import models

from members.models import Member
from sponsors.models import Sponsor


class Race(models.Model):
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
    slogan = models.CharField(max_length=300)
    title = models.CharField(max_length=200, help_text="Title of event. If there are multiple races assoiated to an 'event', make two events.")
    annual = models.CharField(max_length=15)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title and annual. Must be unique.")
    race_type = models.IntegerField(choices=DISCIPLINE_CHOICES, default=RUN)
    sponsors = models.ManyToManyField(Sponsor, related_name='sponsors')
    awards = models.CharField(max_length=300)
    distance = models.CharField(max_length=10, help_text="eg 26.2")
    unit = models.IntegerField(choices=UNIT_CHOICES, default=KM)
    start_datetime = models.DateTimeField(verbose_name="Start Date and Time")
    description = models.TextField()
    course_map = models.URLField(default="http://", blank=True, null=True,
                                 help_text="Link to course map if avail.")
    cut_off = models.CharField(max_length=75, null=True, blank=True,
                               help_text="eg: 13 hours")
    #contact = models.ForeignKey(Member)
    contacts = models.ManyToManyField(Member, related_name='contacts')

    location = models.TextField()
    location_iframe = models.TextField(blank=True, null=True)
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps or other mapping software pointing towards the start location")
    reg_url = models.URLField(default="http://", blank=True, null=True,
                              help_text="Link to registartion flyer or to registration URL for online signup.")
    reg_description = models.TextField()
    entry_form = models.FileField(upload_to="races/entry_forms", null=True, blank=True)
    discounts = models.TextField(blank=True, null=True,
                                 help_text="Describe discounts for the race if they exist.")
    lodging = models.URLField(default="http://", blank=True, null=True,
                              help_text="link to lodging information.")
    packet_pickup = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('race_detail', (), {'year': self.start_datetime.strftime("%Y"),
                                    'month': self.start_datetime.strftime("%b").lower(),
                                    'day': self.start_datetime.strftime("%d"),
                                    'slug': self.slug})

    @property
    def get_overall_results(self):
        return self.result_set.all().order_by('time')

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
    def get_race_news(self):
        return News.objects.filter(race=self, draft=2).order_by('-pub_date')

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

class News(models.Model):
    DRAFT = 1
    PUBLIC = 2
    DRAFT_CHOICES = (
        (DRAFT, "Draft",),
        (PUBLIC, "Public",),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    race = models.ForeignKey(Race)
    body = models.TextField()
    draft = models.IntegerField(choices=DRAFT_CHOICES)

    class Meta:
        verbose_name_plural = "Latest Race Updates"

    def __unicode__(self):
        return self.slug

    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), {'year': self.start_datetime.strftime("%Y"),
                                    'month': self.start_datetime.strftime("%b").lower(),
                                    'day': self.start_datetime.strftime("%d"),
                                    'slug': self.slug})

class EmergencyContact(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=13)
    address = models.TextField()
    relationship = models.CharField(max_length=40)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Racer(models.Model):
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
    trailhawk = models.ForeignKey(Member, unique=True, null=True, blank=True,
                             help_text="If racer is a trailhawk select profile.")
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    shirt_size = models.IntegerField(choices=SIZE_CHOICES, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    state = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    contact = models.ForeignKey(EmergencyContact, verbose_name="Emergency Contact", blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)

    @models.permalink
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('racer_detail', (), {'object_id': self.pk})

    @property
    def get_results(self):
        return Result.objects.filter(racer=self)

    @property
    def age(self):
        TODAY = datetime.date.today()
        return  (TODAY.year - self.birth_date.year)

    @property
    def get_gender(self):
        for num, gender in self.GENDER_CHOICES:
            if num == self.gender:
                return gender


class Result(models.Model):
    racer = models.ForeignKey(Racer)
    race = models.ForeignKey(Race)
    bib_number = models.IntegerField()
    time = models.CharField(max_length=20, null=True, blank=True)
    place = models.CharField(max_length=25, null=True, blank=True,
                             help_text='Ex. First Overall Male or First Masters Female')
    course_record = models.BooleanField()
    dq = models.BooleanField(verbose_name="Disqualified")

    def __unicode__(self):
        return "%s - %s - %s" % (self.racer, self.race.title, self.time)


class Report(models.Model):

    report = models.URLField(default="http://",
                             help_text="Link to race report")
    title = models.CharField(max_length=200)
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)

    def __unicode__(self):
        return self.title
