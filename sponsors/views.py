from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Sponsor


class SponsorDetailView(DetailView):
    model = Sponsor


class SponsorListView(ListView):
    model = Sponsor
