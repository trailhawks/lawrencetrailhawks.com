from django.db import models
from django.contrib.auth.models import User

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

    race_name = models.CharField(max_length=200,
                                 help_text="Name of race.")
    annual = models.CharField(max_length=25,
                              help_text="Inagural, second, third, etc...")
    slug = models.SlugField(unique=True,
                            help_text="Prepopulated from Race Name and Annual. Must be unique.")
    race_type = models.IntegerField(choices=DISCIPLINE_CHOICES, default=RUN)
    race_date = models.DateField()
    distance = models.IntegerField()
    unit = models.IntegerField(choices=UNIT_CHOICES, default=KM)
    loops = models.IntegerField(default=1,
                                help_text="Number of loops for the race. If a Point-to-Point set loops = 0.")
   

    def __unicode__(self):
        return self.slug
    
    @models.permalink
    def get_absolute_url(self):
        return ('result_detail', (), { 'year': self.race_date.strftime("%Y"),
                                      'month': self.race_date.strftime("%b").lower(),
                                      'day': self.race_date.strftime("%d"),
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
    
    
    
class Racer(models.Model):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE,"Male"),
        (FEMALE,"Female"),
    )
    
    name = models.CharField(max_length=40, help_text="Name of racer")
    user = models.ForeignKey(User, unique=True, null=True, blank=True,
                             help_text="If user exists in our system link it to a user profile.")
    gender = models.IntegerField(choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)
    
    def __unicode__(self):
        return self.name

class Result(models.Model):
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)
    bib_number = models.IntegerField()
    time = models.TimeField()
    place = models.CharField(max_length=25, null=True, blank=True, 
                             help_text='Ex. First Overall Male or First Masters Female')
    
class Report(models.Model):
    
    report = models.URLField(default="http://",
                             help_text="Link to race report")
    title = models.CharField(max_length=200)
    race = models.ForeignKey(Race)
    racer = models.ForeignKey(Racer)
    
    def __unicode__(self):
        return self.title