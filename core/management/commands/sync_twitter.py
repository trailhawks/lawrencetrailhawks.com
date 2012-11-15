import logging

from django.core.management.base import NoArgsCommand

from core.syncer import sync_twitter


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):

    def handle(self, **options):
        logger.info('syncing recent twitter messages')
        try:
            sync_twitter()
            logger.info('done syncing recent twitter messages')
        except Exception as e:
            logger.exception(e)
