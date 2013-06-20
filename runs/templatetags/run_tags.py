from django.template import Library

from ..models import Run


register = Library()


@register.assignment_tag(takes_context=True)
def get_todays_runs(context):
    return {
        'todays_run': Run.objects.today(),
        'next_run': Run.objects.next()
    }


@register.assignment_tag(takes_context=True)
def get_weekly_runs(context):
    return Run.objects.active()
