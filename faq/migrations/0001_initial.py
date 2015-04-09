# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('-content_type',),
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
    ]
