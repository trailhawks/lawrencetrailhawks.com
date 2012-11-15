import logging

from django.core.management.base import NoArgsCommand
from core.syncer import sync_flickr_all


logger = logging.getLogger(__name__)


class Command(NoArgsCommand):

    def handle(self, **options):
        logger.info('syncing all flickr photos')
        try:
            sync_flickr_all()
            logger.info('done syncing all flickr photos')
        except Exception as e:
            logger.exception(e)
