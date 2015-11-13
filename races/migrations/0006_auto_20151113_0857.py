# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0005_auto_20151110_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='title',
            field=models.CharField(help_text='Title of event. If there are multiple races assoiated to an "event", make two events.', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='race',
            name='unit',
            field=models.IntegerField(default=1, null=True, blank=True, choices=[(1, 'Kilometers'), (2, 'Miles')]),
            preserve_default=True,
        ),
    ]
