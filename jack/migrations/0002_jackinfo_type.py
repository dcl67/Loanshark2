# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-26 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jackinfo',
            name='type',
            field=models.CharField(default='Data', max_length=10),
        ),
    ]
