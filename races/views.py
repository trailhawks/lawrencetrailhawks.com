from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.races.models import Race
from django.views.generic.date_based import object_detail, archive_index
import datetime


def upcoming_events(request):
    queryset = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('-start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="events/event_archive.html", allow_future=True)
    return HttpResponse(a)
    
