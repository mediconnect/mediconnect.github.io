# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0003_hospital_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='review_number',
        ),
    ]