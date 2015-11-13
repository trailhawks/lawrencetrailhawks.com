# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0007_race_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='annual',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
    ]
