from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200, help_text="Title of event. If there are multiple races assoiated to an 'event', make two events.")
    annual = models.CharField(max_length=15)
    slug = models.SlugField(unique=True,
                            help_text="Suggested value automatically generated from title. Must be unique.")
    
    date = models.DateTimeField()
    contact_email = models.EmailField(help_text="Email of contact")
    contact_phone = models.PositiveIntegerField(help_text="ex. 7856668888")
    location = models.TextField()
    map_link = models.URLField(default="http://",
                               help_text="Link to google maps or other mapping software pointing towards the start location")
    description = models.TextField()
    reg_url = models.URLField(default="http://",
                              help_text="Link to registartion flyer or to registration URL for online signup.")
    reg_description = models.TextField()
    awards = models.CharField(max_length=300)
    packet_pickup = models.TextField(blank=True, null=True)
    
    
    class Meta:
        verbose_name_plural = "Events"
        ordering = ['-date']
    
    def __unicode__(self):
        return self.slug
        
    @models.permalink    
    def get_absolute_url(self):
        return ('event_detail', (), { 'year': self.date.strftime("%Y"),
                                      'month': self.date.strftime("%b").lower(),
                                      'day': self.date.strftime("%d"),
                                      'slug': self.slug } )
                                      
