from django.views.generic import dates
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Race, Racer


class RaceMixin(object):
    queryset = Race.objects.all()
    date_field = 'start_datetime'
    allow_future = True


class RaceIndex(RaceMixin, dates.ArchiveIndexView):
    make_object_list = True
    pass


class RaceYear(RaceMixin, dates.YearArchiveView):
    pass


class RaceMonth(RaceMixin, dates.MonthArchiveView):
    pass


class RaceDay(RaceMixin, dates.DayArchiveView):
    pass


class RaceDateDetail(RaceMixin, dates.DateDetailView):
    queryset = Race.objects.all()


class RaceResultDetail(RaceMixin, dates.DateDetailView):
    queryset = Race.objects.all()
    template_name = 'races/race_result.html'


class RacerDetailView(DetailView):
    model = Racer


class RacerListView(ListView):
    model = Racer
