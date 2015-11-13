# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0006_auto_20151113_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='background',
            field=ajaximage.fields.AjaxImageField(help_text='Optional background photo', null=True, blank=True),
            preserve_default=True,
        ),
    ]
