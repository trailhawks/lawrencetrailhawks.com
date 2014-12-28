import logging

from races.models import Race


logger = logging.getLogger(__name__)


def host_(request):
    logger.debug('host::{0}'.format(request.get_host()))


def host_race(request, race):
    logger.debug('race::{0}'.format(race))
    try:
        request.race = Race.objects.get(slug=race)
    except Race.DoesNotExist:
        request.race = None
