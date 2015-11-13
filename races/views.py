from django.views.generic import dates, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Race, Racer


class RaceMixin(object):
    queryset = Race.objects.all()
    date_field = 'start_datetime'
    allow_future = True
    navitem = 'races'


class RaceIndex(TemplateView):
    template_name = 'races/races.html'
    navitem = 'races'

    def get_context_data(self, **kwargs):
        context = super(RaceIndex, self).get_context_data(**kwargs)
        context['completed_races'] = Race.objects.complete().order_by('-start_datetime')
        context['upcoming_races'] = Race.objects.upcoming().order_by('start_datetime')
        return context


#class RaceIndex(RaceMixin, dates.ArchiveIndexView):
#    make_object_list = True
#    pass


class RaceUpcomingList(ListView):
    queryset = Race.objects.upcoming()
    template_name = 'races/upcoming.html'
    navitem = 'races'


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


class RacerDetail(DetailView):
    model = Racer
    navitem = 'races'


class RacerList(ListView):
    model = Racer
    navitem = 'races'
