import logging

from events.models import Event
from races.models import Race


logger = logging.getLogger(__name__)


def host_(request):
    logger.debug('host::{0}'.format(request.get_host()))


def host_race(request, slug):
    logger.debug('event::{0}'.format(slug))

    if '.' in slug:
        slug = slug.split('.')[0]

    try:
        event = Event.objects.get(slug=slug)
        request.event = event
        if event.races.count():
            request.race = event.races.latest('start_datetime')
    except Event.DoesNotExist:
        request.event = None

    logger.debug('race::{0}'.format(slug))
    if not hasattr(request, 'race'):
        try:
            race = Race.objects.get(slug=slug)
            request.race = race
        except Race.DoesNotExist:
            race = Race.objects.get(slug='hawk-100-mile-50-mile-marathon-fifth-annual')
            request.race = race
