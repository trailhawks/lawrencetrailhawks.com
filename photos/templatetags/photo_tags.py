from django.template import Library, Node, TemplateSyntaxError, Variable, VariableDoesNotExist

from syncr.flickr.models import Photo


register = Library()


class SearchPhotoNode(Node):
    def __init__(self, machine_tags, num, varname):
        self.machine_tags = Variable(machine_tags)
        self.num = num
        self.varname = varname

    def render(self, context):
        try:
            machine_tags = self.machine_tags.resolve(context)
            context[self.varname] = Photo.objects.filter(tags__name__in=machine_tags).order_by('?')[:self.num]
        except (VariableDoesNotExist, Exception):
            pass

        return ''


@register.tag
def get_photos_by_machine_tags(parser, token):
    bits = token.contents.split()
    if len(bits) != 5:
        raise TemplateSyntaxError("get_photos_by_machine_tags tag takes exactly four arguments")
    if bits[3] != 'as':
        raise TemplateSyntaxError("third argument to get_photos_by_machine_tags tag must be 'as'")
    return SearchPhotoNode(bits[1], bits[2], bits[4])
