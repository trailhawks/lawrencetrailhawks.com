from django.contrib.contenttypes.models import ContentType
from django.template import Library

from ..models import FAQ


register = Library()


@register.assignment_tag(takes_context=True)
def get_faqs_by_content_type(context, content_type, ):
    app_label, model = content_type.split('.')
    content_type = ContentType.objects.get(app_label=app_label, model=model)
    return FAQ.objects.filter(content_type=content_type)


@register.assignment_tag(takes_context=True)
def get_latest_faqs(context, num):
    return FAQ.objects.all()[:num]
