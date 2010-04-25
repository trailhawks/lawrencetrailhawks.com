from lawrencetrailhawks.races.models import Race, Result, Racer
from lawrencetrailhawks.runs.models import Run
from syncr.twitter.models import Tweet
from django.contrib.auth.models import User
from members.models import Member
import datetime, csv

def get_latest():
    tweets = Tweet.objects.all().order_by('-pub_time')
    
    return {
            "tweets" : tweets,
           }
           
