# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields
from django.conf import settings
import core.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('hawk_name', models.CharField(max_length=50, null=True, blank=True)),
                ('phone', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('address2', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100, null=True, blank=True)),
                ('state', models.CharField(max_length=2, null=True, blank=True)),
                ('zip', models.CharField(max_length=25, null=True, blank=True)),
                ('avatar', ajaximage.fields.AjaxImageField(null=True, blank=True)),
                ('date_paid', models.DateField(null=True, blank=True)),
                ('member_since', models.DateField(null=True, blank=True)),
                ('gender', models.IntegerField(blank=True, null=True, choices=[(1, 'Male'), (2, 'Female')])),
                ('notes', models.TextField(null=True, blank=True)),
                ('receive_comment_emails', models.BooleanField(default=False, help_text='Should this member be notified when a comment is left on the website?')),
                ('username', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['last_name'],
                'verbose_name': 'Member',
                'verbose_name_plural': 'Members',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True, blank=True)),
                ('order', models.IntegerField(default=100)),
            ],
            options={
                'verbose_name': 'office',
                'verbose_name_plural': 'offices',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateField()),
                ('end', models.DateField(null=True, blank=True)),
                ('member', models.ForeignKey(blank=True, to='members.Member', null=True)),
                ('office', models.ForeignKey(blank=True, to='members.Office', null=True)),
            ],
            options={
                'verbose_name': 'term',
                'verbose_name_plural': 'terms',
            },
            bases=(models.Model,),
        ),
    ]
