# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-15 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='like_hospitals',
            field=models.ManyToManyField(related_name='_customer_like_hospitals_+', to='customer.Customer'),
        ),
    ]