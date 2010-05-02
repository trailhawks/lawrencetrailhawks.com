from django.core.management.base import NoArgsCommand
from lawrencetrailhawks.lib.syncer import sync_flickr

class Command(NoArgsCommand):
    
    def handle(self, **options):
        print "Syncing flickr..."
        sync_flickr()
        print "Done!"
