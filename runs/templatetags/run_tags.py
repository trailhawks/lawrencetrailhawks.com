from django.template import Library, Node

from ..models import Run


register = Library()


class TodaysRunNode(Node):
    def render(self, context):
        context['todays_run'] = Run.today_objects.all()
        context['next_run'] = Run.next_objects.all()
        return ''


@register.tag
def get_todays_run(parser, token):
    return TodaysRunNode()
