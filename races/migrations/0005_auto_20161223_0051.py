# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0004_race_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='racer',
            name='trailhawk',
            field=models.ForeignKey(blank=True, to='members.Member', help_text='If racer is a trailhawk select profile.', null=True),
        ),
    ]
