from django.db import models

class HawkNews(models.Model):
    DRAFT = 1
    PUBLIC = 2
    DRAFT_CHOICES = (
        (DRAFT,"Draft",),
        (PUBLIC,"Public",),
    )
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    draft = models.IntegerField(choices=DRAFT_CHOICES)
    
    class Meta:
        verbose_name_plural="Hawk News"
    
    def __unicode__(self):
        return self.slug
    
    @models.permalink
    def get_absolute_url(self):
        return ('news_detail', (), { 'year': self.start_datetime.strftime("%Y"),
                                      'month': self.start_datetime.strftime("%b").lower(),
                                      'day': self.start_datetime.strftime("%d"),
                                      'slug': self.slug } )