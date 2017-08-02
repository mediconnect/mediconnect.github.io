# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-31 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0003_auto_20170731_0852'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], default='M', max_length=5)),
                ('category', models.CharField(default='COLD', max_length=50)),
                ('diagnose_hospital', models.CharField(blank=True, max_length=50)),
                ('doctor', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'order_patient',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='patient_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='helper.OrderPatient'),
        ),
    ]
