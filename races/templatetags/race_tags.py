import datetime

from django.template import Library

from ..models import Race, RaceType, Result


register = Library()


@register.filter(name="replace_char")
def replace_char(value, arg):
    """
    Replaces a character with another char
    value = value to be filtered
    arg = string of len 2, first char to be replaced with second char
    """
    return value.replace(arg[0], arg[1])


@register.assignment_tag(takes_context=True)
def get_latest_races(context):
    try:
        return Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime')[0]
    except:
        return None


@register.assignment_tag(takes_context=True)
def get_results_for_race(context, race, race_type=None, gender=None):
    queryset = Result.objects.filter(race=race)
    if race_type:
        queryset = queryset.filter(race_type__pk=race_type.pk)
    if gender:
        queryset = queryset.filter(racer__gender=gender)
    return queryset


@register.assignment_tag(takes_context=True)
def get_race_types_for_race(context, race):
    return RaceType.objects.filter(result__race__pk=race.pk).distinct('name')


@register.inclusion_tag('races/includes/results_table.html', takes_context=True)
def render_results(context, race_results):
    return {
        'race_results': race_results,
    }
