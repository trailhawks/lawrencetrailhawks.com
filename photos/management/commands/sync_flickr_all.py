from django.core.management.base import NoArgsCommand

from lawrencetrailhawks.lib.syncer import sync_flickr_all


class Command(NoArgsCommand):

    def handle(self, **options):
        print "Syncing all of flickr..."
        sync_flickr_all()
        print "Done!"
