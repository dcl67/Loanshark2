# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-26 20:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170518_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='mac_address',
            field=models.ManyToManyField(blank=True, to='inventory.MacAddress'),
        ),
    ]
