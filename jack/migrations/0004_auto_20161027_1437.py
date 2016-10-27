# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 18:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jack', '0003_auto_20161026_1213'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='jackinfo',
            name='portstatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jack.Status'),
        ),
    ]
