from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import News


class NewsDetail(DetailView):
    queryset = News.objects.all()


class NewsList(ListView):
    queryset = News.objects.public()
