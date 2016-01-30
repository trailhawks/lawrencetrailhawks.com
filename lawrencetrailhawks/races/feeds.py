from django_ical.views import ICalFeed

from .models import Race


class RaceFeed(ICalFeed):
    """
    A race event calendar

    """
    product_id = '-//trailhawks.com//Races//EN'
    timezone = 'CST'
    title = 'Lawrence Trail Hawks Race Calendar'

    def items(self):
        return Race.objects.all().order_by('-start_datetime')

    def item_title(self, item):
        return u'{0} {1}'.format(item.annual, item.title)

    def item_description(self, item):
        return item.description

    def item_start_datetime(self, item):
        return item.start_datetime
