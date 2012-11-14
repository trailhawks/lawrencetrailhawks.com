import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic.date_based import object_detail, archive_index
from django.views.generic.list_detail import object_detail as obj_detail
from syncr.flickr.models import Photo

from .models import Race, Racer


def upcoming_races(request):
    queryset = Race.objects.filter(start_datetime__gte=datetime.datetime.now()).order_by('start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="races/upcoming.html", allow_future=True)
    return HttpResponse(a)


def results(request):
    queryset = Race.objects.filter(start_datetime__lte=datetime.datetime.now()).order_by('start_datetime')
    a = archive_index(request, queryset, "start_datetime", template_name="races/results.html")
    return HttpResponse(a)


def race_result(request, *args, **kwargs):
    slug = kwargs.get('slug')
    photos = Photo.objects.filter(tags__contains=slug.replace("-", "")).order_by('?')[0:7]

    year = kwargs.get('year')
    month = kwargs.get('month')
    day = kwargs.get('day')
    slug = kwargs.get('slug')
    queryset = kwargs.get('queryset')
    date_field = kwargs.get('date_field')
    o = object_detail(request, year=year, month=month,
                              day=day, queryset=queryset, date_field=date_field, slug=slug,
                              template_name="races/race_result.html", extra_context={'photos': photos})
    return HttpResponse(o)


def race_detail(request, slug, year, month, day, allow_future, queryset, date_field, extra_context):
    photos = Photo.objects.filter(tags__contains=slug.replace("-", "")).order_by('?')[0:7]

    return object_detail(request,
                         year=year,
                         month=month,
                         day=day,
                         slug=slug,
                         queryset=queryset,
                         date_field=date_field,
                         allow_future=allow_future,
                         extra_context={'photos': photos}
                         )


def racer_detail(request, object_id, queryset):
    person = get_object_or_404(Racer, pk=object_id)
    photos = Photo.objects.filter(tags__icontains=person.first_name).filter(tags__icontains=person.last_name).order_by('?')[0:7]

    return obj_detail(request,
                         queryset=queryset,
                         object_id=object_id,
                         extra_context={'photos': photos}
                         )
