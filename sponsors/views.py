from django.http import HttpResponse
from django.template import Context
from django.template import loader

from lawrencetrailhawks.sponsors.models import Sponsor


def sponsor_list(request):
    object_list = Sponsor.objects.active()
    t = loader.get_template('sponsors/sponsor_list.html')
    c = Context({
        'object_list': object_list,
    })
    return HttpResponse(t.render(c))
