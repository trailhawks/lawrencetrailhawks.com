from syncr.app.tweet import TwitterSyncr
from syncr.app.flickr import FlickrSyncr
from django.conf import settings
from syncr.flickr.models import Photo


def sync_twitter():
    username = settings.TWITTER['username']
    password = settings.TWITTER['password']
    ts = TwitterSyncr(username, password)
    ts.syncUser(username)
    ts.syncTwitterUserTweets(username)


def sync_flickr():
    key = settings.FLICKR['key']
    secret = settings.FLICKR['secret']
    username = settings.FLICKR['username']
    fs = FlickrSyncr(key, secret)
    fs.syncRecentPhotos(username, days=1)
    for photo in Photo.objects.all():
        try:
            fs.syncPhoto(photo.flickr_id)
        except:
            pass
