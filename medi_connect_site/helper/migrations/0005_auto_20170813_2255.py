# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-13 14:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_auto_20170813_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='submit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 13, 14, 55, 35, 422256, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='rank',
            name='disease',
        ),
        migrations.AddField(
            model_name='rank',
            name='disease',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='disease_rank', to='helper.Disease'),
        ),
        migrations.RemoveField(
            model_name='rank',
            name='hospital',
        ),
        migrations.AddField(
            model_name='rank',
            name='hospital',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='hospital_rank', to='helper.Hospital'),
        ),
    ]