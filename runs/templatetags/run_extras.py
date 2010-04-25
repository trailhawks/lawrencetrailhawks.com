from runs.models import Run
from django.template import Library, Node
import datetime
register = Library()
    
class TodaysRunNode(Node):
    def render(self, context):
        context['todays_run'] = Run.objects.filter(run_date=datetime.datetime.now().strftime("%A"))[:0]
        return ''

@register.tag
def get_todays_run(parser, token):
    return TodaysRunNode()
