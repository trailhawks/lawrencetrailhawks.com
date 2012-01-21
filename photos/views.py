from django.http import HttpResponse
from django.template import Context, loader

from syncr.flickr.models import Photo

def photo_test1(request):
    photos = Photo.objects.all().order_by('?')[:8]
    t = loader.get_template('photos.html')
    c = Context({
        "photos": photos,
    })

    return HttpResponse(t.render(c))
