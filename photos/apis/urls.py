from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'photos', views.PhotoViewSet)
router.register(r'random', views.RandomPhotoViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
