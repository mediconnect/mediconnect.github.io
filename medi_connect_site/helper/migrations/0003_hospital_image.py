# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 04:37
from __future__ import unicode_literals

from django.db import migrations, models
import helper.models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_remove_hospital_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='image',
            field=models.ImageField(null=True, upload_to=helper.models.hospital_directory_path),
        ),
    ]