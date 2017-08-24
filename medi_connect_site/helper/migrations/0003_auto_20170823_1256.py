# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 16:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20170820_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='latest_upload',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='submit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 23, 16, 56, 39, 296000, tzinfo=utc)),
        ),
    ]
