# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0005_likehospital'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likehospital',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='likehospital',
            name='hospital',
        ),
        migrations.AddField(
            model_name='likehospital',
            name='hospital',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='helper.Hospital'),
        ),
    ]
