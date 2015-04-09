import logging

from django.core.management.base import BaseCommand

from members.models import Member
from races.models import Racer, Result


logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.normalize_racers()
        self.match_members_to_racers()

    def match_members_to_racers(self):
        racers = Racer.objects.all().order_by('id')
        for racer in racers:
            if not racer.trailhawk:
                try:
                    member = Member.objects.get(first_name=racer.first_name, last_name=racer.last_name)
                    logger.info('{} {}'.format(member.first_name, member.last_name))
                    racer.trailhawk = member
                    racer.save()
                except Member.DoesNotExist:
                    pass
                except Member.MultipleObjectsReturned:
                    logger.error('More than one member exists for: {} {}'.format(racer.first_name, racer.last_name))

    def normalize_racers(self):
        racers = Racer.objects.all().order_by('id')
        for racer in racers:
            racer.first_name = racer.first_name.strip()
            racer.last_name = racer.last_name.strip()
            racer.save()

            # look for duplicate racers....
            racer_values = Racer.objects.filter(first_name=racer.first_name, last_name=racer.last_name).values_list('id', flat=True)
            if len(racer_values) > 1:
                logger.info(racer_values)
                logger.info(Result.objects.filter(racer_id__in=racer_values).count())
                first = True
                Result.objects.filter(racer_id__in=racer_values).update(racer_id=racer_values[0])
                for racer_id in racer_values:
                    if first:
                        first = False
                    else:
                        logger.info('deleting: {}'.format(racer_id))
                        Racer.objects.filter(id=racer_id).delete()
