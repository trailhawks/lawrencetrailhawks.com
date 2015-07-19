# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0003_race_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='number',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
