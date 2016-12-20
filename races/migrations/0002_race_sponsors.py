# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='sponsors',
            field=models.ManyToManyField(related_name='sponsors', to='sponsors.Sponsor'),
            preserve_default=True,
        ),
    ]
