from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Links


class LinkDetailView(DetailView):
    model = Links
    navitem = 'links'


class LinkListView(ListView):
    model = Links
    navitem = 'links'
