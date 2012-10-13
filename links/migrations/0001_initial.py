# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Links'
        db.create_table('links_links', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('link', self.gf('django.db.models.fields.URLField')(default='http://', max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('links', ['Links'])


    def backwards(self, orm):
        # Deleting model 'Links'
        db.delete_table('links_links')


    models = {
        'links.links': {
            'Meta': {'object_name': 'Links'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['links']