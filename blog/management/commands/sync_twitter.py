from __future__ import absolute_import

from django.conf import settings
from django.core.management.base import NoArgsCommand

from syncr.app.tweet import TwitterSyncr


def sync_twitter():
    username = settings.TWITTER['username']
    password = settings.TWITTER['password']
    ts = TwitterSyncr(username, password)
    ts.syncUser(username)
    ts.syncTwitterUserTweets(username)


class Command(NoArgsCommand):

    def handle(self, **options):
        print "Syncing twitter...."
        sync_twitter()
        print "Done!"
