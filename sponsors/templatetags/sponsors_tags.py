from django.template import Library

from ..models import Sponsor


register = Library()


@register.assignment_tag(takes_context=True)
def get_sponsors(context, num):
    return Sponsor.active_objects.all()[:num]
