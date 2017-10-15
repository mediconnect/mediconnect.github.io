# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-15 02:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0003_auto_20171014_2104'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderpatient',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='orderpatient',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='last_name',
        ),
    ]
