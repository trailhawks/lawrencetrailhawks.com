from django.conf import settings
from django.core.management.base import NoArgsCommand

from syncr.app.flickr import FlickrSyncr


def sync_flickr_all():
    key = settings.FLICKR['key']
    secret = settings.FLICKR['secret']
    username = settings.FLICKR['username']
    fs = FlickrSyncr(key, secret)
    fs.syncAllPublic(username)


class Command(NoArgsCommand):

    def handle(self, **options):
        print "Syncing flickr BITCHES!!..."
        sync_flickr_all()
        print "Done!"
