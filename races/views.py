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
    queryset = Race.objects.filter(start_datetime__lte=datetime.datetime.now()).order_by('start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="races/results.html")
    return HttpResponse(a)
    
def race_result(request, *args, **kwargs):
    year = kwargs.get('year')
    month = kwargs.get('month')
    day = kwargs.get('day')
    slug = kwargs.get('slug')
    queryset = kwargs.get('queryset')
    date_field=kwargs.get('date_field')
    o = object_detail(request, year=year, month=month, day=day, queryset=queryset, date_field=date_field, slug=slug, template_name="races/race_result.html")
    return HttpResponse(o)
    
 
    
    
