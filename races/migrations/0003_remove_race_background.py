# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_race_sponsors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='race',
            name='background',
        ),
    ]
