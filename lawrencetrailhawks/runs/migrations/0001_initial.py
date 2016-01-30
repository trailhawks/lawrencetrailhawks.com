# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title. Must be unique.', unique=True)),
                ('day_of_week', models.IntegerField(default=0, choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('run_time', models.CharField(help_text='Time of run (ex. 6:30 PM)', max_length=25)),
                ('details', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('contact', models.ForeignKey(to='members.Member')),
                ('location', models.ForeignKey(blank=True, to='locations.Location', null=True)),
            ],
            options={
                'ordering': ['day_of_week'],
                'verbose_name': 'Run',
                'verbose_name_plural': 'Runs',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
    ]
