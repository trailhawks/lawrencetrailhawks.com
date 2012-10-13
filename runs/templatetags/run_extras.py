import datetime

from django.template import Library, Node

from runs.models import Run


register = Library()


class TodaysRunNode(Node):
    def render(self, context):
        todays_run = Run.objects.filter(day_of_week=datetime.datetime.now().weekday())
        if len(todays_run) > 0:
            context['todays_run'] = Run.objects.get(day_of_week=datetime.datetime.now().weekday())
        return ''


@register.tag
def get_todays_run(parser, token):
    return TodaysRunNode()
