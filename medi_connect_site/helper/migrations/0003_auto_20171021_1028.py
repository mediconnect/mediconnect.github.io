# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20171019_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='trans_status',
            field=models.CharField(choices=[(0, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe6\x9c\xaa\xe5\xbc\x80\xe5\xa7\x8b'), (1, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (2, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xae\xa1\xe6\xa0\xb8\xe4\xb8\xad'), (4, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8'), (3, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe9\xa9\xb3\xe5\x9b\x9e'), (5, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (6, b'\xe8\x8b\xb1\xe8\xaf\x91\xe6\xb1\x89\xe6\x9c\xaa\xe5\xbc\x80\xe5\xa7\x8b'), (7, b'\xe8\x8b\xb1\xe8\xaf\x91\xe6\xb1\x89\xe8\xbf\x9b\xe8\xa1\x8c\xe4\xb8\xad'), (8, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xae\xa1\xe6\xa0\xb8\xe4\xb8\xad'), (10, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xb7\xb2\xe5\xae\xa1\xe6\xa0\xb8'), (9, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe9\xa9\xb3\xe5\x9b\x9e'), (11, b'\xe6\xb1\x89\xe8\xaf\x91\xe8\x8b\xb1\xe5\xb7\xb2\xe5\xae\x8c\xe6\x88\x90'), (12, b'\xe8\xae\xa2\xe5\x8d\x95\xe5\xae\x8c\xe6\x88\x90')], default=0, max_length=20),
        ),
    ]
