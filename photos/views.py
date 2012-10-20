from django.http import HttpResponse
from django.template import Context, loader

from syncr.flickr.models import Photo


def photo_list(request):
    photos = Photo.objects.all().order_by('?')[:12]
    t = loader.get_template('photos/photo_list.html')
    c = Context({
        'photos': photos,
    })

    return HttpResponse(t.render(c))
