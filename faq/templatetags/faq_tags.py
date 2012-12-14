from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.template import Library

from ..models import FAQ


register = Library()


@register.assignment_tag(takes_context=True)
def get_faqs_by_content_type(context, content_type):
    app_label, model = content_type.split('.')
    ct = ContentType.objects.get(app_label=app_label, model=model)
    return FAQ.objects.filter(content_type=ct)


@register.assignment_tag(takes_context=True)
def get_faqs_for_object(context, obj):
    queryset = FAQ.objects.filter(Q(content_type__app_label=obj._meta.app_label) & Q(Q(object_id__isnull=True) or Q(object_id=obj.pk)))
    return queryset


@register.assignment_tag(takes_context=True)
def get_latest_faqs(context, num):
    return FAQ.objects.all()[:num]
