import datetime

from django.template import Library, Node

from runs.models import Run

register = Library()

class TodaysRunNode(Node):
    def render(self, context):
        todays_run = Run.objects.filter(run_date=datetime.datetime.now().strftime("%A"))
        if len(todays_run) > 0:
            context['todays_run'] = Run.objects.get(run_date=datetime.datetime.now().strftime("%A"))
        return ''

@register.tag
def get_todays_run(parser, token):
    return TodaysRunNode()
