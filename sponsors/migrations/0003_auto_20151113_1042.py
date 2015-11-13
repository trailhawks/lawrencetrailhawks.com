# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_sponsor_homepage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='homepage',
            field=models.BooleanField(default=False, verbose_name='Show on homepage?'),
            preserve_default=True,
        ),
    ]
