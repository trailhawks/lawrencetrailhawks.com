# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0004_race_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='facebook_event_url',
            field=models.URLField(help_text='Link to Facebook Event page', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='race',
            name='facebook_url',
            field=models.URLField(help_text='Link to Facebook page', null=True, blank=True),
            preserve_default=True,
        ),
    ]
