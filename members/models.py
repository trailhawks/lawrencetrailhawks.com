from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    username = models.ForeignKey(User, unique=True)
    hawk_name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    address = models.TextField()
    avatar = models.ImageField(upload_to="members/avatars", blank=True,null=True)
    active = models.BooleanField()
    date_paid = models.DateField()
    
    # class Meta:
    #     verbose_name_plural = "Members"
    
    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

        
    @models.permalink   
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('member_detail', (), { 'object_id': self.pk } )
        