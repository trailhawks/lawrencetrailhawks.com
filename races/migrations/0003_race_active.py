# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0002_auto_20150406_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
