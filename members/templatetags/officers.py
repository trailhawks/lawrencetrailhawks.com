from __future__ import absolute_import

from django.template import Library, Node

from .models import Member


register = Library()

class OfficerNode(Node):
    def render(self, context):
        president = Member.objects.get(position=1)
        vice_president = Member.objects.get(position=2)
        treasurer = Member.objects.get(position=3)
        secretary = Member.objects.get(position=4)
        web_master = Member.objects.get(position=5)
        context['officers'] = {"president": president,
                               "vice_president": vice_president,
                               "treasurer": treasurer,
                               "secretary": secretary,
                               "web_master": web_master}
        return ''

@register.tag
def get_officers(parser, token):
    return OfficerNode()
