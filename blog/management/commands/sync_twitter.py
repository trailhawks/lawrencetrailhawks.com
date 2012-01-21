from django.core.management.base import NoArgsCommand

from lawrencetrailhawks.lib.syncer import sync_twitter


class Command(NoArgsCommand):

    def handle(self, **options):
        print "Syncing twitter...."
        sync_twitter()
        print "Done!"
