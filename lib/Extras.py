from lawrencetrailhawks.races.models import Race, Result, Racer
from lawrencetrailhawks.runs.models import Run
from syncr.twitter.models import Tweet
from django.contrib.auth.models import User

from members.models import Member


import datetime, csv

def get_latest():
    latest_event = []#Event.objects.filter(date__gte=datetime.datetime.now()).order_by('date').latest('date')
    todays_run =[]# Run.objects.filter(run_date=datetime.datetime.now().strftime("%A")).latest('run_date')
    other_news = ""
    tweets = Tweet.objects.all()
    return {"latest_event": latest_event,
            "todays_run": todays_run,
            "other_news": other_news,
            "tweets" : tweets,
           }
           


def load_users():
    from data.user_data import users
    for user in users:
        u,created = User.objects.get_or_create(username=user[0],email=user[0], first_name=user[1], last_name=user[2])
        if created:
            print "User created:",u
        else:
            print "Found user:",u

def load_members():
    from data.member_data import members
    for member in members:
        m,created = Member.objects.get_or_create(username=member[0], hawk_name=member[1], phone=member[2], address=member[3], active=member[4], date_paid=member[5])
        if created:
            print "Member created:",m
        else:
            print "Found member:",m
            
def load_racers(racers):
    for racer in racers:
        r,created = Racer.objects.get_or_create(name=racer[0], gender=racer[1], email=racer[2])
        if created:
            print "Racer created:", r
        else:
            print "Racer found:", r
        
def load_race(race):
    r,created = Race.objects.get_or_create(logo = race['logo'],
                                           slogan = race['slogan'],
                                           title =race['title'],
                                           annual =  race['annual'],
                                           slug = race['slug'],
                                           race_type = race['race_type'],
                                           awards = race['awards'],
                                           distance = race['distance'],
                                           unit =race['unit'],
                                           loops = race['loops'],
                                           start_datetime =race['start_datetime'] ,
                                           description = race['description'],
                                           course_map = race['course_map'],
                                           cut_off = race['cut_off'],
                                           contact = race['contact'],
                                           location = race['location'],
                                           map_link = race['map_link'],
                                           reg_url =race['reg_url'],
                                           reg_description =race['reg_description'],
                                           entry_form = race['entry_form'],
                                           discounts = race['discounts'],
                                           lodging = race['lodging'],
                                           packet_pickup = race['packet_pickup'],)
    if created:
        print "Race created:",r
    else:
        print "Race found:", r
                                          
def load_data():
    load_users()
    load_members()
    from data.racers import racers
    for racer in racers:
        load_racers(racer)
    from data.races import races
    for race in races:
        load_race(race)   