# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0005_auto_20171015_1556'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='staff',
            options={},
        ),
        migrations.AddField(
            model_name='staff',
            name='sequence',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
