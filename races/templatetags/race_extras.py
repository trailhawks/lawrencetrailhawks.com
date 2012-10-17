import datetime

from django.template import Library, Node

from blog.models import Post
from races.models import Race

register = Library()


@register.filter(name="replace_char")
def replace_char(value, arg):
    """
    Replaces a character with another char
    value = value to be filtered
    arg = string of len 2, first char to be replaced with second char
    """
    return value.replace(arg[0], arg[1])


class LatestRaceNode(Node):
    def render(self, context):
        try:
            context['latest_race'] = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime').latest('start_datetime')
        except:
            latest_post = Post.published_objects.all()
            if len(latest_post):
                context['latest_post'] = latest_post[0]
            else:
                context['latest_post'] = []
        return ''


@register.tag
def get_latest_race(parser, token):
    return LatestRaceNode()
