from __future__ import absolute_import

import datetime

from django.template import Library, Node

from ..models import Run


register = Library()

class TodaysRunNode(Node):
    def render(self, context):
        day_of_week = datetime.datetime.now().strftime("%A")
        todays_run = Run.objects.filter(run_date=day_of_week)
        if len(todays_run) > 0:
            context['todays_run'] = Run.objects.get(run_date=day_of_week)
        return ''

@register.tag
def get_todays_run(parser, token):
    return TodaysRunNode()
