# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Location', fields ['slug']
        db.delete_unique(u'locations_location', ['slug'])


        # Changing field 'Location.slug'
        db.alter_column(u'locations_location', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Location.slug'
        raise RuntimeError("Cannot reverse this migration. 'Location.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Location.slug'
        db.alter_column(u'locations_location', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True))
        # Adding unique constraint on 'Location', fields ['slug']
        db.create_unique(u'locations_location', ['slug'])


    models = {
        u'locations.location': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Location'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '6', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'zoom': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['locations']