from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import FAQ


class FaqDetailView(DetailView):
    model = FAQ
    navitem = 'faqs'


class FaqListView(ListView):
    model = FAQ
    navitem = 'faqs'
