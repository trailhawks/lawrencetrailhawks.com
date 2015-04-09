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
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('body', models.TextField()),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Draft'), (2, 'Public')])),
                ('alert_status', models.CharField(default='', max_length=50, blank=True, choices=[('', 'Default no style.'), ('success', 'success'), ('info', 'info'), ('warning', 'warning'), ('danger', 'danger')])),
                ('object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('content_type', models.ForeignKey(blank=True, to='contenttypes.ContentType', null=True)),
            ],
            options={
                'ordering': ('-pub_date',),
                'get_latest_by': 'pub_date',
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
            bases=(core.models.ShortUrlMixin, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='news',
            unique_together=set([('slug', 'pub_date')]),
        ),
    ]
