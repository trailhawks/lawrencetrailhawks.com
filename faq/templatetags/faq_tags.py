from django.contrib.contenttypes.models import ContentType
from django.db.models import get_model
from django.template import Library, Node, TemplateSyntaxError

register = Library()


class RandomFaqNode(Node):
    def __init__(self, num, varname):
        self.num, self.varname = num, varname
        self.model = get_model('faq', 'Faq')

    def render(self, context):
        context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''


@register.tag
def get_latest_faqs(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError("get_latest_faqs tag takes exactly three arguments")

    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to get_latest_faqs tag must be 'as'")

    return RandomFaqNode(bits[1], bits[3])


class FaqByContentTypeNode(Node):
    def __init__(self, content_type, varname):
        app_label, model = content_type.split('.')

        self.content_type = ContentType.objects.get(app_label=app_label, model=model)
        self.varname = varname
        self.model = get_model('faq', 'Faq')

    def render(self, context):
        context[self.varname] = self.model._default_manager.filter(content_type=self.content_type)
        return ''


@register.tag
def get_faqs_by_content_type(parser, token):
    bits = token.contents.split()
    if len(bits) != 4:
        raise TemplateSyntaxError("get_faqs_by_content_type tag takes exactly three arguments")

    if bits[2] != 'as':
        raise TemplateSyntaxError("second argument to get_faqs_by_content_type tag must be 'as'")

    return FaqByContentTypeNode(bits[1], bits[3])
