from lawrencetrailhawks.events.models import Event
from lawrencetrailhawks.runs.models import Runs
import datetime

def get_latest():
	latest_event = Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date')
	if latest_event: 
	    latest_event = latest_event[0]
	else:
	    latest_event = []
	
	todays_run = Runs.objects.filter(run_date=datetime.datetime.now().strftime("%A"))
	other_news = ""
	print todays_run
	return {"latest_event": latest_event,
	        "todays_run": todays_run,
	        "other_news": other_news,
	       }
