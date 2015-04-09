from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Run


class RunDetail(DetailView):
    model = Run
    navitem = 'runs'
    slug_field = 'slug'


class RunList(ListView):
    model = Run
    navitem = 'runs'

    def get_queryset(self):
        return super(RunList, self).get_queryset().active()
