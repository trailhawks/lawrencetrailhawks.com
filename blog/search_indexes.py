from __future__ import absolute_import

from haystack import indexes

from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='publish')
    tags = indexes.MultiValueField(model_attr='tags')

    def get_model(self):
        return Post

    def prepare_tags(self, obj):
        return [tag for tag in obj.tags.split(' ') if tag]
