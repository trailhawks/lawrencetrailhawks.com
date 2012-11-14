import csv

from django.core.management.base import BaseCommand
from optparse import make_option
from races.models import Race, RaceType, Racer, Result


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('-r', '--race', help="race id or slug"),
        make_option('-c', '--csv', help="path to csv file to be loaded"),
    )

    def handle(self, *args, **options):
        _race = options.pop('race', None)
        print _race

        if not _race:
            raise Exception("You forgot to add the race silly")

        try:
            race_id = int(_race)
            race = Race.objects.get(pk=race_id)

        except ValueError:
            race_slug = _race
            race = Race.objects.get(slug=race_slug)

        _csv = options.pop('csv')

        if not _csv:
            raise Exception("You forgot the csv silly")

        result_data = self.load_csv(_csv)

        for row in result_data:
            defaults = {}
            race_type = None
            time = row[1]
            place = row[5]

            if row[4] == "M":
                gender = 1
            else:
                gender = 2

            racer, created = Racer.objects.get_or_create(first_name=row[2], last_name=row[3], gender=gender)

            if len(row[6]):
                race_type, created = RaceType.objects.get_or_create(name=row[6])

            if 'DNS' in time:
                defaults['dns'] = True

            if 'DNF' in time:
                defaults['dnf'] = True

            if 'CR' in place:
                defaults['course_record'] = True

            print "Found Racer: %s" % racer
            try:
                result, _ = Result.objects.get_or_create(race=race, racer=racer, time=row[1], bib_number=row[0], place=place, defaults=defaults)
            except IndexError:
                result, _ = Result.objects.get_or_create(race=race, racer=racer, time=row[1], bib_number=row[0], defaults=defaults)

            if race_type:
                result.race_type = race_type
                result.save()

            print "Result for %s for race: %s" % (racer, race)
            print result

        print "results loaded"

    def load_csv(self, path):
        c = csv.reader(open(path, 'r'))
        return c
