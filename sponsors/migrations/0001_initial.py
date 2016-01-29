# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from name. Must be unique.', null=True, blank=True)),
                ('url', models.URLField(help_text='URL to website')),
                ('address', models.TextField(null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('logo', ajaximage.fields.AjaxImageField(null=True, blank=True)),
                ('discount_detail', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField(default=False)),
                ('homepage', models.BooleanField(default=False, verbose_name='Show on homepage?')),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
            bases=(models.Model,),
        ),
    ]
