from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Sponsor


class SponsorDetailView(DetailView):
    queryset = Sponsor.active_objects.all()


class SponsorListView(ListView):
    queryset = Sponsor.active_objects.all()
