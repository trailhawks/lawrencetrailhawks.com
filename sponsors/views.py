from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Sponsor


class SponsorDetailView(DetailView):
    queryset = Sponsor.objects.all()
    navitem = 'sponsors'


class SponsorListView(ListView):
    queryset = Sponsor.objects.active().order_by('slug')
    navitem = 'sponsors'
