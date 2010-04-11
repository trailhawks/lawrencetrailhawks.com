from django.db import models
from lawrencetrailhawks.members.models import Member

class Run(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")
    run_date = models.CharField(max_length=25, 
                                help_text="Day of run (ex. Monday)")
    run_time = models.CharField(max_length=25,
                                help_text="Time of run (ex. 6:30 PM)")
    location = models.TextField()
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps location")
    details = models.TextField()
    contact = models.ForeignKey(Member)
    
    class Meta:
        verbose_name_plural = "Runs"
    
    @models.permalink   
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('run_detail', (), { 'slug': self.slug } )
    
    def __unicode__(self):
        return self.name
    