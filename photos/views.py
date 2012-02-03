from __future__ import absolute_import

from django.http import HttpResponse
from django.template import Context
from django.template import loader

from syncr.flickr.models import Photo


def photo_list(request, template_name='photos/photo_list.html'):
    photos = Photo.objects.all().order_by('?')[:8]
    t = loader.get_template(template_name)
    c = Context({
        'photos': photos,
    })
    return HttpResponse(t.render(c))
