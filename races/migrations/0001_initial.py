# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ajaximage.fields
import core.models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField()),
                ('relationship', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Emergency Contact',
                'verbose_name_plural': 'Emergency Contacts',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('enable_comments', models.BooleanField(default=True)),
                ('title', models.CharField(help_text='Title of event. If there are multiple races assoiated to an "event", make two events.', max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('number', models.IntegerField(null=True, blank=True)),
                ('annual', models.CharField(max_length=15, null=True, blank=True)),
                ('slug', models.SlugField(help_text='Suggested value automatically generated from title and annual. Must be unique.', unique=True)),
                ('slogan', models.CharField(max_length=300, null=True, blank=True)),
                ('logo', ajaximage.fields.AjaxImageField(null=True, blank=True)),
                ('background', ajaximage.fields.AjaxImageField(help_text='Optional background photo', null=True, blank=True)),
                ('race_type', models.IntegerField(default=1, choices=[(1, 'Run'), (2, 'Bike'), (3, 'Swim')])),
                ('awards', models.TextField(null=True, blank=True)),
                ('distance', models.CharField(help_text='eg 26.2', max_length=100, null=True, blank=True)),
                ('unit', models.IntegerField(default=1, null=True, blank=True, choices=[(1, 'Kilometers'), (2, 'Miles')])),
                ('start_datetime', models.DateTimeField(verbose_name='Start Date and Time')),
                ('description', models.TextField()),
                ('course_map', models.URLField(help_text='Link to course map if avail.', null=True, blank=True)),
                ('cut_off', models.CharField(help_text='eg: 13 hours', max_length=75, null=True, blank=True)),
                ('reg_url', models.URLField(help_text='Link to registartion flyer or to registration URL for online signup.', null=True, blank=True)),
                ('reg_description', models.TextField(null=True, blank=True)),
                ('entry_form', models.FileField(null=True, upload_to='races/entry_forms', blank=True)),
                ('discounts', models.TextField(help_text='Describe discounts for the race if they exist.', null=True, blank=True)),
                ('lodging', models.URLField(help_text='Link to lodging information', null=True, blank=True)),
                ('packet_pickup', models.TextField(null=True, blank=True)),
                ('facebook_url', models.URLField(help_text='Link to Facebook page', null=True, blank=True)),
                ('facebook_event_url', models.URLField(help_text='Link to Facebook Event page', null=True, blank=True)),
                ('location', models.ForeignKey(blank=True, to='locations.Location', null=True)),
                ('race_directors', models.ManyToManyField(to='members.Member')),
            ],
            options={
                'ordering': ['-start_datetime'],
                'verbose_name': 'Race',
                'verbose_name_plural': 'Races',
            },
            bases=(models.Model, core.models.ShortUrlMixin),
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('phone', models.CharField(max_length=13, null=True, blank=True)),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('shirt_size', models.IntegerField(blank=True, null=True, choices=[(1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL')])),
                ('birth_date', models.DateField(null=True, blank=True)),
                ('city', models.CharField(max_length=40, null=True, blank=True)),
                ('state', models.CharField(max_length=40, null=True, blank=True)),
                ('country', models.CharField(max_length=40, null=True, blank=True)),
                ('contact', models.ForeignKey(verbose_name='Emergency Contact', blank=True, to='races.EmergencyContact', null=True)),
                ('trailhawk', models.ForeignKey(null=True, blank=True, to='members.Member', help_text='If racer is a trailhawk select profile.', unique=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
                'verbose_name': 'Racer',
                'verbose_name_plural': 'Racers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RaceType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
                ('reg_date', models.DateField(verbose_name='Registration Date')),
                ('end_date', models.DateField(null=True, verbose_name='End Date', blank=True)),
                ('reg_cost', models.IntegerField(verbose_name='Registration Cost')),
                ('race', models.ForeignKey(to='races.Race')),
            ],
            options={
                'verbose_name': 'Registration Dates',
                'verbose_name_plural': 'Registration Dates',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('report', models.URLField(help_text='Link to race report')),
                ('title', models.CharField(max_length=200)),
                ('race', models.ForeignKey(to='races.Race')),
                ('racer', models.ForeignKey(to='races.Racer')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bib_number', models.IntegerField()),
                ('time', models.CharField(max_length=20, null=True, blank=True)),
                ('place', models.TextField(help_text='Ex. First Overall Male or First Masters Female', null=True, blank=True)),
                ('course_record', models.BooleanField(default=False)),
                ('dq', models.BooleanField(default=False, verbose_name='Disqualified')),
                ('dns', models.BooleanField(default=False, verbose_name='Did not Start')),
                ('dnf', models.BooleanField(default=False, verbose_name='Did not Finish')),
                ('race', models.ForeignKey(to='races.Race')),
                ('race_type', models.ForeignKey(blank=True, to='races.RaceType', help_text='For races with multiple race types.', null=True)),
                ('racer', models.ForeignKey(to='races.Racer')),
            ],
            options={
                'ordering': ('time',),
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
            bases=(models.Model,),
        ),
    ]
