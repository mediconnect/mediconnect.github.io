# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-21 21:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import helper.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_1', models.PositiveSmallIntegerField(default=0)),
                ('week_2', models.PositiveSmallIntegerField(default=0)),
                ('week_3', models.PositiveSmallIntegerField(default=0)),
                ('week_4', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='unknown', max_length=50)),
                ('category', models.CharField(default='unknown', max_length=50)),
                ('keyword', models.CharField(default='unknown', max_length=150)),
            ],
            options={
                'db_table': 'disease',
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_not_trans', models.FileField(blank=True, upload_to=helper.models.order_directory_path)),
                ('case_trans', models.FileField(blank=True, upload_to=helper.models.order_directory_path)),
                ('feedback_not_trans', models.FileField(blank=True, upload_to=helper.models.order_directory_path)),
                ('feedback_trans', models.FileField(blank=True, upload_to=helper.models.order_directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('area', models.CharField(blank=True, max_length=50)),
                ('slots_open', models.IntegerField(default=20)),
                ('website', models.URLField(blank=True)),
                ('introduction', models.TextField(default='intro')),
                ('specialty', models.TextField(default='specialty')),
                ('feedback_time', models.CharField(default='one week', max_length=50)),
                ('price_range', models.CharField(default='unknown', max_length=50)),
            ],
            options={
                'db_table': 'hospital',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_time', models.DateField(default=datetime.date.today)),
                ('estimate_feedback', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, choices=[(0, 'started'), (1, 'submitted'), (2, 'received'), (3, 'feedback'), (4, 'paid')], max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
                ('disease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Disease')),
                ('document_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Document')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Hospital')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('OTHER', 'Other')], default='M', max_length=5)),
                ('category', models.CharField(choices=[('CANCER', 'Cancer'), ('COLD', 'Cold')], default='COLD', max_length=50)),
                ('diagnose_hospital', models.TextField(blank=True)),
                ('doctor', models.TextField(blank=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField(default=0)),
                ('disease', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='helper.Disease')),
                ('hospital', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='helper.Hospital')),
            ],
            options={
                'db_table': 'rank',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Patient'),
        ),
        migrations.AddField(
            model_name='document',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Order'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helper.Hospital'),
        ),
    ]
