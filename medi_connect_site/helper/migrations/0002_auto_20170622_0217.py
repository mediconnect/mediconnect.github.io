# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 02:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0002_auto_20170622_0119'),
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='approved',
        ),
        migrations.RemoveField(
            model_name='document',
            name='extra_document',
        ),
        migrations.RemoveField(
            model_name='document',
            name='submit',
        ),
        migrations.RemoveField(
            model_name='document',
            name='supervisor',
        ),
        migrations.RemoveField(
            model_name='document',
            name='translator',
        ),
        migrations.RemoveField(
            model_name='document',
            name='upload',
        ),
        migrations.RemoveField(
            model_name='order',
            name='estimate_feedback',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_time',
        ),
        migrations.AddField(
            model_name='document',
            name='is_origin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='document',
            name='is_translated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='document',
            name='upload_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='feedback',
            field=models.ManyToManyField(related_name='feedback_file', to='helper.Document'),
        ),
        migrations.AddField(
            model_name='order',
            name='origin',
            field=models.ManyToManyField(related_name='original_file', to='helper.Document'),
        ),
        migrations.AddField(
            model_name='order',
            name='pending',
            field=models.ManyToManyField(related_name='pending_file', to='helper.Document'),
        ),
        migrations.AddField(
            model_name='order',
            name='receive',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='submit',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='order',
            name='trans_status',
            field=models.CharField(blank=True, choices=[(0, 'not_started'), (1, 'ongoing'), (2, 'approving'), (3, 'approved'), (4, 'disapproved'), (5, 'finished')], max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='translator_C2E',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chinese_translator', to='translator.Translator'),
        ),
        migrations.AddField(
            model_name='order',
            name='translator_E2C',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='english_translator', to='translator.Translator'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[(0, 'started'), (1, 'submitted'), (2, 'translating_origin'), (3, 'received'), (4, 'return'), (5, 'translating_feedback'), (6, 'feedback'), (7, 'PAID')], max_length=20),
        ),
    ]
