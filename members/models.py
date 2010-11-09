from django.db import models

from django.contrib.auth.models import User
import datetime

class Member(models.Model):
    PRESIDENT = 1
    VICE_PRESIDENT = 2
    TREASURER = 3
    SECRETARY = 4
    WEB_MASTER = 5
    POSITION_CHOICES = (
        (PRESIDENT, "President"),
        (VICE_PRESIDENT, "Vice President"),
        (TREASURER, "Treasurer"),
        (SECRETARY, "Secretary"),
        (WEB_MASTER, "Web Master"),
    )

    GENDER_CHOICES = (
        (1, "Male"),
        (2, "Female"),
    )    

    username = models.ForeignKey(User, null=True, blank=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    hawk_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to="members/avatars", blank=True,null=True)
    active = models.BooleanField()
    date_paid = models.DateField(null=True, blank=True)
    member_since = models.DateField(null=True, blank=True)
    position = models.IntegerField(choices=POSITION_CHOICES, null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    
    # class Meta:
    #     verbose_name_plural = "Members"
    
    def __unicode__(self):
        if self.hawk_name == " ":
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return "%s \"%s\" %s" % (self.first_name, self.hawk_name, self.last_name)
   
        
    @models.permalink   
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('member_detail', (), { 'object_id': self.pk } )
    
    @property
    def position_name(self):
        if self.position:
            return dict(Member.POSITION_CHOICES)[self.position]

    @property
    def date_expires(self):
        date_expires = datetime.date(self.date_paid.year+1, self.date_paid.month, self.date_paid.day)
        return date_expires
        
    @property
    def full_hawk_name(self):
        if self.hawk_name in [" ", "a"]:
            return "%s %s" % (self.first_name, self.last_name)
        else:
            return "%s \"%s\" %s" % (self.first_name, self.hawk_name, self.last_name)
    
    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)
    
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
