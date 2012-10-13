# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HawkNews'
        db.create_table('hawknews_hawknews', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('draft', self.gf('django.db.models.fields.IntegerField')(default=2)),
        ))
        db.send_create_signal('hawknews', ['HawkNews'])


    def backwards(self, orm):
        # Deleting model 'HawkNews'
        db.delete_table('hawknews_hawknews')


    models = {
        'hawknews.hawknews': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'HawkNews'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'draft': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['hawknews']