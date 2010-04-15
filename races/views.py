from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.races.models import Race, Racer, RaceResult, RaceReport
import datetime



def get_results(request):
    race = Race.objects.get(pk=1)
    results = RaceResult.objects.all()
    t = loader.get_template('results/race_detail.html')
    c = Context({
        "results" : results,
    })
    
    return HttpResponse(t.render(c))
    
