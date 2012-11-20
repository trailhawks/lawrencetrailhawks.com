from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Run


class RunDetailView(DetailView):
    model = Run
    slug_field = 'slug'


class RunListView(ListView):
    model = Run
