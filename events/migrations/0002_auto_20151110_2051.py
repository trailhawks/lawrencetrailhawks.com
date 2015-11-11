# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='facebook_event_url',
            field=models.URLField(help_text='Link to Facebook Event page', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='facebook_url',
            field=models.URLField(help_text='Link to Facebook page', null=True, blank=True),
            preserve_default=True,
        ),
    ]
