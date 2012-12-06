from django.template import Library

from syncr.flickr.models import Photo


register = Library()


@register.assignment_tag(takes_context=True)
def get_photos_by_machine_tags(context, machine_tags, num):
    return Photo.objects.filter(tags__name__in=machine_tags).order_by('?')[:num]


@register.assignment_tag(takes_context=True)
def get_photos_count_by_machine_tags(context, machine_tags):
    return Photo.objects.filter(tags__name__in=machine_tags).all().count()
