from django.core.management.base import NoArgsCommand
from lawrencetrailhawks.lib.syncer import sync_twitter, sync_flickr

class Command(NoArgsCommand):
    
    def handle(self, **options):
        print "Syncing twitter...."
        sync_twitter()
        print "Done!"
        print "*"*10
        print "Syncing flickr..."
        sync_flickr()
        print "Done!"
