# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-23 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20170622_0217'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
