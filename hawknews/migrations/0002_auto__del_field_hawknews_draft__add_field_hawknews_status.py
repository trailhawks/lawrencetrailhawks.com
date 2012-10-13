# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'HawkNews.draft'
        db.rename_column('hawknews_hawknews', 'draft', 'status')

    def backwards(self, orm):
        # Adding field 'HawkNews.draft'
        db.rename_column('hawknews_hawknews', 'status', 'draft')

    models = {
        'hawknews.hawknews': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'HawkNews'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['hawknews']
