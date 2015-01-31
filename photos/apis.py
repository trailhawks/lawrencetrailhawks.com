from rest_framework import viewsets
from syncr.flickr.models import Photo

from .serializers import PhotoSerializer


class PhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows photos to be viewed.
    """
    queryset = Photo.objects.filter(active=True)
    serializer_class = PhotoSerializer


class RandomPhotoViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows photos to be viewed.
    """
    queryset = Photo.objects.filter(active=True).order_by('?')
    serializer_class = PhotoSerializer
