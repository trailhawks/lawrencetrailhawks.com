from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.races.models import Race, Racer
from django.views.generic.date_based import object_detail, archive_index
import datetime


def upcoming_races(request):
    queryset = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('-start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="races/upcoming.html", allow_future=True)
    return HttpResponse(a)
    
def results(request):
    queryset = Race.objects.filter(start_datetime__lte=datetime.datetime.now()).order_by('-start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="races/results.html")
    return HttpResponse(a)
    
 
    
    
