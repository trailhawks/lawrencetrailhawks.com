from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.template import Library

from ..models import Sponsor


register = Library()


@register.assignment_tag(takes_context=True)
def get_sponsors_by_content_type(context, content_type):
    app_label, model = content_type.split('.')
    ct = ContentType.objects.get(app_label=app_label, model=model)
    return Sponsor.objects.active().filter(content_type=ct)


@register.assignment_tag(takes_context=True)
def get_sponsors_for_object(context, obj):
    """Find Sponsors for an object and all model types."""
    query = Q(content_type__app_label=obj._meta.app_label, object_id=obj.pk)
    query = query | Q(content_type__app_label=obj._meta.app_label, object_id__isnull=True)
    queryset = Sponsor.objects.active().filter(query)
    return queryset


@register.assignment_tag(takes_context=True)
def get_latest_sponsors(context, num=10):
    return Sponsor.objects.active()[:num]


@register.assignment_tag(takes_context=True)
def get_homepage_sponsors(context, num=10):
    return Sponsor.objects.homepage().order_by('?')[:num]
