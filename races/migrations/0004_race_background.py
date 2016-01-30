# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flickr', '0002_photo_active'),
        ('races', '0003_remove_race_background'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='background',
            field=models.ForeignKey(blank=True, to='flickr.Photo', null=True),
            preserve_default=True,
        ),
    ]
