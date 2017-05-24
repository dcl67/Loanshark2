# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-18 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='hostname',
        ),
        migrations.RemoveField(
            model_name='device',
            name='f_id',
        ),
        migrations.AddField(
            model_name='device',
            name='serial_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
