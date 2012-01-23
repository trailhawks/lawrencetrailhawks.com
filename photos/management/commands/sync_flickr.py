
from django.conf import settings
from django.core.management.base import NoArgsCommand

from syncr.app.flickr import FlickrSyncr
from syncr.flickr.models import Photo


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


class Command(NoArgsCommand):

    def handle(self, **options):
        print "Syncing flickr BITCHES!!..."
        sync_flickr()
        print "Done!"
