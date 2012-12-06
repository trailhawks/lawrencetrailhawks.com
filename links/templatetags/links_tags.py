from django.template import Library

from ..models import Links


register = Library()


@register.assignment_tag(takes_context=True)
def get_links(context):
    return Links.board.all()
