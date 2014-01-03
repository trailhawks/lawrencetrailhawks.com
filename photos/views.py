from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from syncr.flickr.models import Photo


class PhotoDetailView(DetailView):
    model = Photo
    navitem = 'photos'


class PhotoListView(ListView):
    model = Photo
    navitem = 'photos'
    paginate_by = 12
