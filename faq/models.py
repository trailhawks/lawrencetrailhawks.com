from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        """docstring for get_absolute_url"""
        return ('faq_detail', (), {'object_id': self.pk})
