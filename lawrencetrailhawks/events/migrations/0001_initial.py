# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('body', models.TextField()),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Draft'), (2, 'Public')])),
                ('facebook_url', models.URLField(help_text='Link to Facebook page', null=True, blank=True)),
                ('facebook_event_url', models.URLField(help_text='Link to Facebook Event page', null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
    ]
