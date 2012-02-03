from __future__ import absolute_import

from haystack import indexes

from syncr.flickr.models import Photo


class PhotoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='taken_date')
    tags = indexes.MultiValueField(model_attr='tags')

    def get_model(self):
        return Photo

    def prepare_tags(self, obj):
        return [tag for tag in obj.tags.split(' ') if tag]
