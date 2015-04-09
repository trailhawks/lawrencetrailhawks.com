import sys

from django.conf import settings
from django.template import Library
from libthumbor import CryptoURL
from syncr.flickr.models import Photo
from urlparse import urlparse


register = Library()


@register.filter(name="remove_http")
def remove_http(value):
    """
    Replaces a character with another char
    value = value to be filtered
    arg = string of len 2, first char to be replaced with second char
    """
    value = value.replace('http://', '')
    value = value.replace('https://', '')
    return value


@register.assignment_tag(takes_context=True)
def get_photos_by_machine_tags(context, machine_tags, num=10, random=False):
    queryset = Photo.objects.active().filter(tags__name__in=machine_tags)
    if random:
        queryset = queryset.order_by('?')
    return queryset[:num]


@register.assignment_tag(takes_context=True)
def get_photos_count_by_machine_tags(context, machine_tags):
    return Photo.objects.active().filter(tags__name__in=machine_tags).all().count()


def thumb(url, **kwargs):
    """
    Inspired by:
        http://tech.yipit.com/2013/01/03/how-yipit-scales-thumbnailing-with-thumbor-and-cloudfront/

    returns a thumbor url for 'url' with **kwargs as thumbor options.

    Positional arguments:
    url -- the location of the original image

    Keyword arguments:
    For the complete list of thumbor options
    https://github.com/globocom/thumbor/wiki/Usage
    and the actual implementation for the url generation
    https://github.com/heynemann/libthumbor/blob/master/libthumbor/url.py

    """
    THUMBOR_BASE_URL = getattr(settings, 'THUMBOR_BASE_URL', None)
    THUMBOR_KEY = getattr(settings, 'THUMBOR_KEY', 'MY_SECURE_KEY')

    if THUMBOR_BASE_URL:
        base = THUMBOR_BASE_URL
    else:
        # otherwise assume that thumbor is setup behind the same
        # CDN behind the `thumbor` namespace.
        scheme, netloc = urlparse.urlsplit(url)[:2]
        base = '{}://{}/thumbor'.format(scheme, netloc)
    crypto = CryptoURL(key=THUMBOR_KEY)

    # just for code clarity
    thumbor_kwargs = kwargs
    if not 'fit_in' in thumbor_kwargs:
        thumbor_kwargs['fit_in'] = True

    thumbor_kwargs['image_url'] = url
    path = crypto.generate(**thumbor_kwargs)

    return u'{}{}'.format(base, path)


#@register.simple_tag
#def thumbor_url(image_url, **kwargs):
#    return thumb(image_url, **kwargs)
