from django.template import Library, Node
from django.template import TemplateSyntaxError

from blog.models import Post


register = Library()


class LatestBlogNode(Node):
    def __init__(self, num, varname):
        self.num, self.varname = num, varname

    def render(self, context):
        context[self.varname] = Post.published_objects.all()[:self.num]
        return ''


@register.tag
def get_latest_posts(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError("get_latest_posts tag takes exactly three arguments")
    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to get_latest_posts tag must be 'as'")
    return LatestBlogNode(bits[1], bits[3])
