from lawrencetrailhawks.events.models import Event
from lawrencetrailhawks.runs.models import Runs
from syncr.twitter.models import Tweet
import datetime

def get_latest():
    latest_event = Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date').latest('date')
    todays_run = Runs.objects.filter(run_date=datetime.datetime.now().strftime("%A")).latest('run_date')
    other_news = ""
    tweets = Tweet.objects.all()
    return {"latest_event": latest_event,
            "todays_run": todays_run,
            "other_news": other_news,
            "tweets" : tweets,
           }
           

    
