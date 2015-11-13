from django.template import Library

from ..models import Member


register = Library()


@register.assignment_tag(takes_context=True)
def get_active_members(context):
    return Member.objects.current()


@register.assignment_tag(takes_context=True)
def get_officers(context):
    return Member.board_objects.all()
