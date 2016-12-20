from django.db.models.signals import post_save

from news.models import News
from django_posse.providers import update_providers


post_save.connect(update_providers, sender=News, dispatch_uid="publish_news")
