from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from syncr.flickr.models import Photo, PhotoSet


class PhotoDetailView(DetailView):
    model = Photo
    navitem = 'photos'
    template_name = 'photos/photo_detail.html'


class PhotoListView(ListView):
    model = Photo
    navitem = 'photos'
    paginate_by = 12
    template_name = 'photos/photo_list.html'


class PhotoSetDetailView(DetailView):
    model = PhotoSet
    navitem = 'photosets'
    template_name = 'photos/photoset_detail.html'


class PhotoSetListView(ListView):
    model = PhotoSet
    navitem = 'photosets'
    paginate_by = 12
    template_name = 'photos/photoset_list.html'
