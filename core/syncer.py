from django.conf import settings

from syncr.flickr.models import Photo


def sync_flickr():
    from syncr.app.flickr import FlickrSyncr

    key = settings.FLICKR['key']
    secret = settings.FLICKR['secret']
    username = settings.FLICKR['username']
    fs = FlickrSyncr(key, secret)
    fs.syncRecentPhotos(username, days=1)
    for photo in Photo.objects.all():
        try:
            fs.syncPhoto(photo.flickr_id)
        except Exception, e:
            print e


def sync_flickr_all():
    from syncr.app.flickr import FlickrSyncr

    key = settings.FLICKR['key']
    secret = settings.FLICKR['secret']
    username = settings.FLICKR['username']
    fs = FlickrSyncr(key, secret)
    fs.syncAllPublic(username)
    for photo in Photo.objects.all():
        try:
            fs.syncPhoto(photo.flickr_id)
        except Exception, e:
            print e


def sync_twitter():
    from syncr.app.tweet import TwitterSyncr

    username = settings.TWITTER['username']
    password = settings.TWITTER['password']
    ts = TwitterSyncr(username, password)
    ts.syncUser(username)
    ts.syncTwitterUserTweets(username)
