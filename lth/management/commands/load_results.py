from __future__ import absolute_import

import csv

from django.core.management.base import BaseCommand
from optparse import make_option

from races.models import Race
from races.models import Racer
from races.models import Result


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('-r', '--race', help="race id or slug"),
        make_option('-c', '--csv', help="path to csv file to be loaded"),
        )

    def handle(self, *args, **options):
        _race = options.pop('race', None)
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
            if row[4] == "M":
                gender = 1
            else:
                gender = 2

            racer, created = Racer.objects.get_or_create(first_name=row[2], last_name=row[3], gender=gender)
            print "Found Racer: %s" % racer
            try:
                result = Result.objects.get_or_create(race=race, racer=racer, time=row[1], bib_number=row[0], place=row[5])
            except IndexError:
                result = Result.objects.get_or_create(race=race, racer=racer, time=row[1], bib_number=row[0])
            print "Result for %s for race: %s" % (racer, race)
            print result
        print "results loaded"

    def load_csv(self, path):
        c = csv.reader(open(path, 'r'))
        return c
