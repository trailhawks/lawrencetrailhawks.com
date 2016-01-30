from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.template import Library

from ..models import News


register = Library()


@register.assignment_tag(takes_context=True)
def get_news_by_content_type(context, content_type):
    app_label, model = content_type.split('.')
    ct = ContentType.objects.get(app_label=app_label, model=model)
    return News.objects.public().filter(content_type=ct)


@register.assignment_tag(takes_context=True)
def get_news_for_object(context, obj):
    """Find News for an object and all model types."""
    query = Q(content_type__app_label=obj._meta.app_label, object_id=obj.pk)
    query = query | Q(content_type__app_label=obj._meta.app_label, object_id__isnull=True)
    queryset = News.objects.public().filter(query)
    return queryset


@register.assignment_tag(takes_context=True)
def get_latest_news(context, num=10):
    return News.objects.public()[:num]


@register.assignment_tag(takes_context=True)
def get_latest_news_for_object(context, obj):
    """Find latest News for an object and all model types."""
    query = Q(content_type__app_label=obj._meta.app_label, object_id=obj.pk)
    query = query | Q(content_type__app_label=obj._meta.app_label, object_id__isnull=True)
    queryset = News.objects.public().recent().filter(query)
    return queryset
