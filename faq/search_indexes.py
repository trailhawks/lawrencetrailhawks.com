from __future__ import absolute_import

import datetime

from haystack import indexes

from .models import FAQ


class FAQIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pub_date = indexes.DateTimeField()
    tags = indexes.MultiValueField()

    def get_model(self):
        return FAQ

    def prepare_pub_date(self, obj):
        return datetime.datetime.now()

    def prepare_tags(self, obj):
        return []
        #return [tag for tag in obj.tags.split(' ') if tag]
