from __future__ import absolute_import

import datetime

from django.template import Library, Node

from ..models import Race
from blog.models import Post


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
            latest_race = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime').latest('start_datetime')
            context['latest_race'] = latest_race
        except Race.DoesNotExist:
            context['latest_race'] = None

        try:
            latest_post = context['latest_post'] = Post.objects.all().order_by('-publish')
            context['latest_post'] = latest_post
        except Post.DoesNotExist:
            context['latest_post'] = None

        return ''


@register.tag
def get_latest_race(parser, token):
    return LatestRaceNode()
