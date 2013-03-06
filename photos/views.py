from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from syncr.flickr.models import Photo


class PhotoDetailView(DetailView):
    model = Photo


class PhotoListView(ListView):
    model = Photo
    paginate_by = 12
