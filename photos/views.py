from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
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


class PhotoReview(LoginRequiredMixin, ListView):
    navitem = 'photos'
    paginate_by = 20
    template_name = 'photos/photo_review_list.html'

    def get_queryset(self):
        return Photo.objects.active()

    def post(self, request):
        action = request.POST['action']
        page = request.POST['page']
        photo_id = request.POST['photo_id']

        photo = get_object_or_404(Photo, pk=photo_id)

        if action == 'enable':
            photo.active = True
            photo.save()
            success_message = 'Your photo has been hidden.'
            messages.add_message(self.request, messages.SUCCESS, success_message)
        elif action == 'disable':
            photo.active = False
            photo.save()
            success_message = 'Your photo is now visible.'
            messages.add_message(self.request, messages.SUCCESS, success_message)
        redirect_url = reverse('photo_review_list') + '?page=' + page
        return HttpResponseRedirect(redirect_url)


class PhotoSetDetailView(DetailView):
    model = PhotoSet
    navitem = 'photosets'
    template_name = 'photos/photoset_detail.html'


class PhotoSetListView(ListView):
    model = PhotoSet
    navitem = 'photosets'
    paginate_by = 12
    template_name = 'photos/photoset_list.html'
