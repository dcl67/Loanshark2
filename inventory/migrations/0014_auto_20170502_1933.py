# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-02 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20170502_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='printer',
            name='make',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='printer',
            name='model',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='appliance',
            name='appliance_name',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
