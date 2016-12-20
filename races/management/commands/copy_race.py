import click
import logging

from datetime import datetime
from django.utils.text import slugify
from django_docopt_command import DocOptCommand

from faq.models import FAQ
from races.models import Race


__doc__ = """Usage:
copy_race [--race=<race>] [--number=<number>]

Options:
  -h --help         Show this screen.
  --version         Show version.
  --race=<race_id>  Race ID or Race slug to associate the results with.
  --number=<number> Race number.
"""


logger = logging.getLogger(__name__)


class Command(DocOptCommand):
    docs = __doc__

    def prepare_date(self, date_str):
        try:
            date_obj = datetime.strptime(date_str, '%m/%d/%Y')
            return date_obj
        except ValueError:
            return False

        return False

    def get_race(self, id_str):
        try:
            return Race.objects.get(id=int(id_str))
        except (ValueError, Race.DoesNotExist):
            return False

    def gather_information(self, race_id, number):
        click.echo('Hello there! We are going to copy a race now.')

        # get race
        if not race_id:
            races = Race.objects.all().order_by('-start_datetime')
            for race in races:
                click.echo('{0}. {1}'.format(race.pk, race.title))

            race = self.get_race(click.prompt("First, give me the ID of the Race object we're gonna copy. If there is more than one race already, give me ID of the latest one."))
        else:
            race = self.get_race(race_id)

        while not race:
            race = self.get_race(click.prompt("Wrong ID! Try again"))

        # get number
        if not number:
            number = click.prompt("What is the number of the race? If this is a second race, write 2. If third, then 3. You got it")

        date = self.prepare_date(click.prompt("What is the date of this new race? (Format: MM/DD/YYYY)"))
        while not date:
            date = self.prepare_date(click.prompt("Wrong format! Provide a date in format: MM/DD/YYYY)"))

        return (race, number, date)

    def handle_docopt(self, arguments):
        number = arguments.get('--number')
        race_id = arguments.get('--race')

        (race, number, date) = self.gather_information(race_id, number)

        click.echo("OK! That's it. Now I'll copy your race.")

        number = int(number)
        title = unicode('{} #{}'.format(str(race), str(number)))
        race_id = race.id

        new_race = race
        new_race.pk = None
        new_race.id = None
        new_race.title = title
        new_race.slug = slugify(title)
        new_race.start_datetime = date
        new_race.active = True
        new_race.save()

        race = self.get_race(race_id)

        # copy RDs
        race_directors = race.race_directors.all()
        for race_director in race_directors:
            new_race.race_directors.add(race_director)

        # copy FAQs
        faqs = FAQ.objects.filter(content_type__app_label=race._meta.app_label, object_id=race.pk)
        for faq in faqs:
            faq.pk = None
            faq.id = None
            faq.object_id = new_race.id
            faq.save()

        # copy Sponsors?

        # race url
        url = new_race.get_absolute_url()
        click.echo("Your race page is ready here: http://trailhawks.com{0}".format(url))
        click.echo("Congrats on yet another race!")
