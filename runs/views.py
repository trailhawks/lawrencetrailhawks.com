from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.runs.models import Run
import datetime

def get_runs_list(request):
    runs = Run.objects.all()
    t = loader.get_template('runs.html')
    c = Context({
        "runs" : runs,
    })
    
    return HttpResponse(t.render(c))
    
    
