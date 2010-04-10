from django.http import HttpResponse
from django.template import Context, loader
from lawrencetrailhawks.events.models import Event
import datetime



def get_event_list(request):
	event_list = Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
	t = loader.get_template('events/upcoming.html')
	c = Context({
		"event_list" : event_list,
	})
	
	return HttpResponse(t.render(c))
	
