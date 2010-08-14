# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Changing field 'Sponsor.phone'
        db.alter_column('sponsors_sponsor', 'phone', self.gf('django.db.models.fields.CharField')(max_length=15))

        # Changing field 'Sponsor.logo'
        db.alter_column('sponsors_sponsor', 'logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100))
    
    
    def backwards(self, orm):
        
        # Changing field 'Sponsor.phone'
        db.alter_column('sponsors_sponsor', 'phone', self.gf('django.db.models.fields.PositiveIntegerField')())

        # Changing field 'Sponsor.logo'
        db.alter_column('sponsors_sponsor', 'logo', self.gf('django.db.models.fields.URLField')(max_length=200))
    
    
    models = {
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'discount_detail': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'default': "'http://'", 'max_length': '200'})
        }
    }
    
    complete_apps = ['sponsors']
