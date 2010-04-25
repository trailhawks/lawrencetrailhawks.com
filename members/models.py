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
    
    username = models.ForeignKey(User)
    hawk_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.TextField()
    avatar = models.ImageField(upload_to="members/avatars", blank=True,null=True)
    active = models.BooleanField()
    date_paid = models.DateField()
    member_since = models.DateField(null=True, blank=True)
    position = models.IntegerField(choices=POSITION_CHOICES, null=True, blank=True)
    
    # class Meta:
    #     verbose_name_plural = "Members"
    
    def __unicode__(self):
           return "%s \"%s\" %s" % (self.username.first_name, self.hawk_name, self.username.last_name)
   
        
    @models.permalink   
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('member_detail', (), { 'object_id': self.pk } )
    
    @property
    def date_expires(self):
        date_expires = datetime.date(self.date_paid.year+1, self.date_paid.month, self.date_paid.day)
        return date_expires
        
    @property
    def full_hawk_name(self):
        return "%s \"%s\" %s" % (self.username.first_name, self.hawk_name, self.username.last_name)
    
    @property
    def full_name(self):
        return "%s %s" % (self.username.first_name, self.username.last_name)
    
    @property
    def email(self):
        return self.username.email
    
    @property
    def president(self):
        return self.objects.get(positon=1)

    @property   
    def vice_president(self):
        return self.objects.get(position=2)

    @property        
    def secretary(self):
        return self.objects.get(position=4)

    @property    
    def treasurer(self):
        return self.objects.get(position=3)
        
    @property        
    def web_master(self):
        return self.objects.get(position=5)