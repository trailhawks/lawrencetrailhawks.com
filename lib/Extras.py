from lawrencetrailhawks.races.models import Race, Result, Racer
from lawrencetrailhawks.runs.models import Run
from syncr.twitter.models import Tweet
from django.contrib.auth.models import User
from members.models import Member
import datetime, csv

def get_latest():
    todays_run = []#Run.objects.filter(run_date=datetime.datetime.now().strftime("%A")).latest('run_date')
    other_news = ""
    tweets = Tweet.objects.all().order_by('-pub_time')
    
    return {"latest_event": latest_event,
            "todays_run": todays_run,
            "other_news": other_news,
            "tweets" : tweets,
           }
           
