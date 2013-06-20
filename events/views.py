from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Event


class EventDetailView(DetailView):
    model = Event
    slug_field = 'slug'


class EventListView(ListView):
    queryset = Event.published_objects.all()
