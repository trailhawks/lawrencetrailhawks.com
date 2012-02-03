from __future__ import absolute_import

from django.http import HttpResponse
from django.template import Context, loader

from .models import FAQ


def get_faq_list(request):
    faq_list = FAQ.objects.all()
    t = loader.get_template('faq.html')
    c = Context({
        'faq_list': faq_list,
    })

    return HttpResponse(t.render(c))
