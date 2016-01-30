from django.conf import settings
from django_thumbor import generate_url
from rest_framework import serializers
from syncr.flickr.models import Photo


CAROUSEL_HEIGHT = getattr(settings, 'CAROUSEL_HEIGHT', 500)
CAROUSEL_WIDTH = getattr(settings, 'CAROUSEL_WIDTH', 1200)
SIDEBAR_HEIGHT = getattr(settings, 'SIDEBAR_HEIGHT', 500)
SIDEBAR_WIDTH = getattr(settings, 'SIDEBAR_WIDTH', 1200)


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    large_url = serializers.SerializerMethodField()
    medium_url = serializers.SerializerMethodField()
    carousel_height = serializers.SerializerMethodField()
    carousel_url = serializers.SerializerMethodField()
    carousel_width = serializers.SerializerMethodField()
    sidebar_height = serializers.SerializerMethodField()
    sidebar_url = serializers.SerializerMethodField()
    sidebar_width = serializers.SerializerMethodField()

    class Meta(object):
        model = Photo
        fields = (
            'flickr_id',
            #'slug',
            'title',
            'description',
            'url',
            'photopage_url',
            'medium_height',
            'medium_width',
            'medium_url',
            'large_height',
            'large_width',
            'large_url',
            'carousel_height',
            'carousel_url',
            'carousel_width',
            'sidebar_height',
            'sidebar_url',
            'sidebar_width',
        )

    def get_medium_url(self, obj):
        return obj.get_medium_url()

    def get_large_url(self, obj):
        return obj.get_large_url()

    def get_carousel_height(self, obj):
        return CAROUSEL_HEIGHT

    def get_carousel_width(self, obj):
        return CAROUSEL_WIDTH

    def get_carousel_url(self, obj):
        return generate_url(obj.get_medium_url(),
                            smart=True,
                            width=CAROUSEL_WIDTH,
                            height=CAROUSEL_HEIGHT)

    def get_sidebar_height(self, obj):
        return SIDEBAR_HEIGHT

    def get_sidebar_width(self, obj):
        return SIDEBAR_WIDTH

    def get_sidebar_url(self, obj):
        return generate_url(obj.get_medium_url(),
                            smart=True,
                            width=SIDEBAR_WIDTH,
                            height=SIDEBAR_HEIGHT)
