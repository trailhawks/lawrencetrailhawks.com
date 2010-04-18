from django.db import models
from races.models import Race

class Event(models.Model):
    race = models.ForeignKey(Race)
    date = models.DateField(null=True, blank=True)
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
                                      
