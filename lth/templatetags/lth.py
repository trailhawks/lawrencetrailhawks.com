import feedparser

from dateutil.parser import *
from dateutil.tz import *
from django.template import Library, Node


register = Library()


class RRCANewsNode(Node):
    def render(self, context):
        d = feedparser.parse('http://feeds.feedburner.com/RRCA-News?format=xml')
        context['rrca_news'] = d['entries'][:4]
        return ''


def get_rrca_news(parser, token):
    return RRCANewsNode()


class TwitterNode(Node):
    def render(self, context):
        d = feedparser.parse('https://api.twitter.com/1/statuses/user_timeline.rss?screen_name=trailhawks')
        raw_tweets = d['entries'][:4]
        tweets = []
        for t in raw_tweets:
            text = t['title'].replace('trailhawks: ', '')
            date = parse(t['updated'])
            tweet = {}
            tweet['text'] = text
            tweet['url'] = t['link']
            tweet['pub_time'] = date.astimezone(gettz())
            tweets.append(tweet)

        context['stweets'] = tweets
        return ''


def get_latest_tweets(parser, token):
    return TwitterNode()

get_latest_tweets = register.tag(get_latest_tweets)
get_rrca_news = register.tag(get_rrca_news)
