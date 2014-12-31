import logging

from events.models import Event
from races.models import Race


logger = logging.getLogger(__name__)


def host_(request):
    logger.debug('host::{0}'.format(request.get_host()))


def host_race(request, slug):
    logger.debug('event::{0}'.format(slug))
    try:
        request.event = Event.objects.get(slug=slug)
    except Event.DoesNotExist:
        request.event = None

    logger.debug('race::{0}'.format(slug))
    try:
        request.race = Race.objects.get(slug=slug)
    except Race.DoesNotExist:
        request.race = None
