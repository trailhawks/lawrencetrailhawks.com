# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Sponsor', fields ['slug']
        db.delete_unique('sponsors_sponsor', ['slug'])

        # Adding field 'Sponsor.content_type'
        db.add_column('sponsors_sponsor', 'content_type',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contenttypes.ContentType'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Sponsor.object_id'
        db.add_column('sponsors_sponsor', 'object_id',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'Sponsor.slug'
        db.alter_column('sponsors_sponsor', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=50, null=True))

    def backwards(self, orm):
        # Deleting field 'Sponsor.content_type'
        db.delete_column('sponsors_sponsor', 'content_type_id')

        # Deleting field 'Sponsor.object_id'
        db.delete_column('sponsors_sponsor', 'object_id')


        # Changing field 'Sponsor.slug'
        db.alter_column('sponsors_sponsor', 'slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=50, unique=True))
        # Adding unique constraint on 'Sponsor', fields ['slug']
        db.create_unique('sponsors_sponsor', ['slug'])


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'sponsors.sponsor': {
            'Meta': {'object_name': 'Sponsor'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']", 'null': 'True', 'blank': 'True'}),
            'discount_detail': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['sponsors']