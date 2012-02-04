from __future__ import absolute_import

from haystack import indexes

from .models import HawkNews


class HawkNewsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date')
    tags = indexes.MultiValueField()

    def get_model(self):
        return HawkNews

    def prepare_tags(self, obj):
        return []
        #return [tag for tag in obj.tags.split(' ') if tag]
