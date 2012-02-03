from __future__ import absolute_import

from django.template import Library, Node
from django.db.models import get_model


register = Library()

class HawkNewsNode(Node):
    def __init__(self, model, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model(*model.split('.'))

    def render(self, context):
        context[self.varname] = self.model._default_manager.filter(draft=2).order_by('-pub_date')[:self.num]
        return ''

@register.tag
def get_latest(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError, "get_latest tag takes exactly four arguments"
    if bits[3] != 'as':
        raise TemplateSyntaxError, "third argument to get_latest tag must be 'as'"
    return HawkNewsNode(bits[1], bits[2], bits[4])
