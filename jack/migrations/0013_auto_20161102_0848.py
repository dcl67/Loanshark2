# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 12:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jack', '0012_auto_20161101_1408'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jackinfo',
            old_name='caller_id',
            new_name='display_name',
        ),
    ]
