# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0008_auto_20151113_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='lodging',
            field=models.URLField(help_text='Link to lodging information', null=True, blank=True),
            preserve_default=True,
        ),
    ]
