# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-25 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20170411_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Licenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_key', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='warrantytype',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='warrantytype',
            name='purchase_date',
        ),
        migrations.AddField(
            model_name='device',
            name='warranty_expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='warranty_purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
