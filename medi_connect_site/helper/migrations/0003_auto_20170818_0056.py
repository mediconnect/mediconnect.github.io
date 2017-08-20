# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 04:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20170808_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='relationship',
            field=models.CharField(choices=[('SELF', 'SELF'), ('RELATIVE', 'RELATIVE'), ('CLIENT', 'CLIENT')], default='SELF', max_length=50),
        ),
        migrations.AlterField(
            model_name='order',
            name='submit',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 18, 4, 56, 8, 997000, tzinfo=utc)),
        ),
    ]