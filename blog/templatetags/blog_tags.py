from django.template import Library

from ..models import Post


register = Library()


@register.assignment_tag(takes_context=True)
def get_latest_posts(context, num):
    return Post.published_objects.all()[:num]
