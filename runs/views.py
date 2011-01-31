from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.list_detail import object_list, object_detail
from django.template import Context, loader
from lawrencetrailhawks.runs.models import Run
import datetime


def run_list(request):
    return object_list(
            request,
            queryset=Run.objects.all())

def run_detail(request, slug):
    return object_detail(
            request,
            queryset=Run.objects.all(),
            slug=slug,
            extra_context = { 'object_list': Run.objects.all()})



def get_runs_list(request):
    runs = Run.objects.all()
    t = loader.get_template('runs.html')
    c = Context({
        "runs" : runs,
    })

    return HttpResponse(t.render(c))


