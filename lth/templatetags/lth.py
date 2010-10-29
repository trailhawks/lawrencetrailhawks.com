import feedparser
from django.template import Library, Node
     
register = Library()
     
class RRCANewsNode(Node):
    def render(self, context):
        d = feedparser.parse("http://feeds.feedburner.com/RRCA-News?format=xml")
        context['rrca_news'] = d['entries'][:4]
        return ''
    
def get_rrca_news(parser, token):
    return RRCANewsNode()

get_rrca_news = register.tag(get_rrca_news)
