from races.models import Race
from django.template import Library, Node
import datetime
register = Library()

@register.filter(name="replace_char")	 	
def replace_char(value, arg):
    """
    Replaces a character with another char
    value = value to be filtered
    arg = string of len 2, first char to be replaced with second char 
    """
    return value.replace(arg[0], arg[1])
    
    
class LatestRaceNode(Node):
    def render(self, context):
        context['latest_race'] = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime').latest('start_datetime')
        return ''

@register.tag
def get_latest_race(parser, token):
    return LatestRaceNode()