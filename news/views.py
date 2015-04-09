from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import News


class NewsDetail(DetailView):
    queryset = News.objects.all()
    navitem = 'news'


class NewsList(ListView):
    queryset = News.objects.public()
    navitem = 'news'
