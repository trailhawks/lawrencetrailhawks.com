# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import core.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug', unique_for_date='publish')),
                ('body', models.TextField(help_text='The body supports Textile markup. Please use http://textile.thresholdstate.com/ to markup the blog post and get the right formatting.', verbose_name='body')),
                ('tease', models.TextField(help_text='Concise text suggested. Does not appear in RSS feed.', verbose_name='tease', blank=True)),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Draft'), (2, 'Public')])),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('repost_url', models.URLField(help_text='URL of original blog posting.', null=True, verbose_name='Original Post', blank=True)),
                ('repost_date', models.DateField(help_text='Date of original blog posting', null=True, verbose_name='Original Post Date', blank=True)),
                ('author', models.ForeignKey(blank=True, to='members.Member', null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
                'db_table': 'blog_posts',
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'get_latest_by': 'publish',
            },
            bases=(core.models.ShortUrlMixin, models.Model),
        ),
    ]
