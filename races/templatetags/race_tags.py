import datetime

from django.template import Library

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


@register.assignment_tag(takes_context=True)
def get_latest_races(context):
    try:
        return Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime').latest('start_datetime')
    except:
        latest_post = Post.published_objects.all()
        if len(latest_post):
            return latest_post[0]
        else:
            return []
