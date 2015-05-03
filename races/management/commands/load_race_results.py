import csv
import logging

from django_docopt_command import DocOptCommand

from races.models import Race, RaceType, Racer, Result


__doc__ = """Usage:
load_race_results --race=<race> --csv=<csv> [--update]

Options:
  -h --help       Show this screen.
  --version       Show version.
  --csv=<csv>     CSV file to load results from.
  --race=<race>   Race ID or Race slug to associate the results with.
"""


logger = logging.getLogger(__name__)


class Command(DocOptCommand):

    docs = __doc__

    def handle_docopt(self, arguments):
        race = arguments['--race']
        csv_filename = arguments['--csv']

        logger.info(race)

        if not csv_filename:
            raise Exception('You forgot the CSV silly')

        if not race:
            raise Exception('You forgot to add the Race silly')

        try:
            race = Race.objects.get(pk=int(race))
        except ValueError:
            race = Race.objects.get(slug=race)

        with open(csv_filename, 'r') as f:
            result_data = list(csv.DictReader(f))

        for row in result_data:
            defaults = {}
            race_type = None
            bib_number = row['bib']
            time = row['time']
            place = row['comments']
            first_name = row['first_name']
            last_name = row['last_name']
            distance = row['distance']

            if row['gender'].strip() in ['m', 'M']:
                gender = 1
            else:
                gender = 2

            racer, _ = Racer.objects.get_or_create(
                first_name=first_name,
                last_name=last_name,
                gender=gender)

            if len(distance):
                race_type, _ = RaceType.objects.get_or_create(
                    name=distance)

            if 'CR' in place:
                defaults['course_record'] = True

            if 'DNF' in time:
                defaults['dnf'] = True

            if 'DNS' in time:
                defaults['dns'] = True

            logger.info('Found Racer: {0}'.format(racer))

            # might update_or_create...
            result, _ = Result.objects.get_or_create(
                race=race,
                racer=racer,
                time=time,
                bib_number=bib_number,
                place=place,
                defaults=defaults)

            if race_type:
                result.race_type = race_type
                result.save()

            logger.info('Result for {0} for race: {1}'.format(racer, race))
            logger.info(result)

        logger.info('results loaded')
