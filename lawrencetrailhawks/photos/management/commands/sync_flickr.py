import logging

from django.core.management.base import NoArgsCommand
from core.syncer import sync_flickr


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):

    def handle(self, **options):
        logger.info('syncing recent flickr photos')
        try:
            sync_flickr()
            logger.info('done syncing recent flickr photos')
        except Exception as e:
            logger.exception(e)
