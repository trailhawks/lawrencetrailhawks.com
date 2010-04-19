from django.http import HttpResponse
from django.template import Context, loader
from syncr.flickr.models import PhotoSet

def photo_test1(request):
    sets = PhotoSet.objects.all()
    print sets
    t = loader.get_template('photos.html')
    c = Context({
        "sets" : sets,
    })
    
    return HttpResponse(t.render(c))