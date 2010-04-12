from django.db import models
from members.models import Member

class Event(models.Model):
    title = models.CharField(max_length=200, help_text="Title of event. If there are multiple races assoiated to an 'event', make two events.")
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")
    date = models.DateTimeField()
    contact = models.ForeignKey(Member)
    location = models.TextField()
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps or other mapping software pointing towards the start location")
    description = models.TextField()
   
    class Meta:
        ordering = ['-date']
    
    def __unicode__(self):
        return self.slug
        
    @models.permalink    
    def get_absolute_url(self):
        return ('event_detail', (), { 'year': self.date.strftime("%Y"),
                                      'month': self.date.strftime("%b").lower(),
                                      'day': self.date.strftime("%d"),
                                      'slug': self.slug } )
                                      
