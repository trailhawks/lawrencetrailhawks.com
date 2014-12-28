from races.models import Race


def host_race(request, race):
    try:
        request.race = Race.objects.get(slug=race)
    except Race.DoesNotExist:
        request.race = None
