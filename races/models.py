from django.db import models
from django.contrib.auth.models import User
from members.models import Member

class Race(models.Model):
    KM = 1
    MI = 2
    UNIT_CHOICES = (
        (KM,"km"),
        (MI,"mi"),
    )
    
    RUN = 1
    BIKE = 2
    SWIM = 3
    DISCIPLINE_CHOICES = (
        (RUN,"Run"),
        (BIKE,"Bike"),
        (SWIM,"Swim"),
    )
    logo = models.ImageField(upload_to="races/logos", blank=True,null=True)
    slogan = models.CharField(max_length=300)
    title = models.CharField(max_length=200, help_text="Title of event. If there are multiple races assoiated to an 'event', make two events.")
    annual = models.CharField(max_length=15)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title and annual. Must be unique.")
    race_type = models.IntegerField(choices=DISCIPLINE_CHOICES, default=RUN)
    awards = models.CharField(max_length=300)
    distance = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES, default=KM)
    loops = models.IntegerField(default=1,
                                help_text="Number of loops for the race. If a Point-to-Point set loops = 0.")
    start_datetime = models.DateTimeField()
    description = models.TextField()
    course_map = models.URLField(default="http://", blank=True, null=True,
                                 help_text="Link to course map if avail.")
    cut_off = models.CharField(max_length=75,
                               help_text="eg: 13 hours")
    contact = models.ForeignKey(Member)
    location = models.TextField()
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps or other mapping software pointing towards the start location")
    reg_url = models.URLField(default="http://", blank=True, null=True,
                              help_text="Link to registartion flyer or to registration URL for online signup.")
    reg_description = models.TextField()
    entry_form = models.FileField(upload_to="races/entry_forms",null=True, blank=True)
    discounts = models.TextField(blank=True, null=True,
                                 help_text="Describe discounts for the race if they exist.")
    lodging = models.URLField(default="http://",
                              help_text="link to lodging information.")
    packet_pickup = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.slug
    
    @models.permalink
    def get_absolute_url(self):
        return ('race_detail', (), { 'year': self.start_datetime.strftime("%Y"),
                                      'month': self.start_datetime.strftime("%b").lower(),
                                      'day': self.start_datetime.strftime("%d"),
                                      'slug': self.slug } )
    
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
    

class RaceNews(models.Model):
    title = models.CharField(max_length=40)
    news_itme = models.TextField()
    race = models.ForeignKey(Race)

    def __unicode__(self):
        return self.title

class Racer(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE,"Male"),
        (FEMALE,"Female"),
    )
    
    name = models.CharField(max_length=40, help_text="Name of racer")
    trailhawk = models.ForeignKey(User, unique=True, null=True, blank=True,
                             help_text="If racer is a trailhawk select profile.")
    email = models.CharField(max_length=50)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Result(models.Model):
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)
    bib_number = models.IntegerField()
    time = models.CommaSeparatedIntegerField(max_length=20)
    place = models.CharField(max_length=25, null=True, blank=True, 
                             help_text='Ex. First Overall Male or First Masters Female')
    course_record = models.BooleanField()
    dq = models.BooleanField()
                             
    def __unicode__(self):
        return "%s - %s - %s"%(self.racer.name,self.race.title, self.time)
    
class Report(models.Model):
    
    report = models.URLField(default="http://",
                             help_text="Link to race report")
    title = models.CharField(max_length=200)
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)
    
    def __unicode__(self):
        return self.title