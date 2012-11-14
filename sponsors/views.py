from django.http import HttpResponse
from django.template import Context, loader
from sponsors.models import Sponsor


def get_sponsors(request):
    sponsors = Sponsor.objects.active()
    t = loader.get_template('sponsors.html')
    c = Context({
        "sponsors": sponsors,
    })

    return HttpResponse(t.render(c))
