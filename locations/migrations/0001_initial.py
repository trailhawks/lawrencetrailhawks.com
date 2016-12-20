# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True)),
                ('zoom', models.IntegerField(default='15', null=True, blank=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Location',
                'verbose_name_plural': 'Location',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
    ]
