from django.template import Library, Node, TemplateSyntaxError

from ..models import News


register = Library()


class LatestHawkNewsNode(Node):
    def __init__(self, num, varname):
        self.num, self.varname = num, varname

    def render(self, context):
        context[self.varname] = News.published_objects.all()[:self.num]
        return ''


@register.tag
def get_latest_news(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError("get_latest_news tag takes exactly three arguments")
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to get_latest_news tag must be 'as'")
    return LatestHawkNewsNode(bits[1], bits[3])
