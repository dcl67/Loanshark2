# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-24 00:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20170518_1541'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout_History',
            fields=[
                ('device_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.Device')),
                ('checkout_time', models.DateTimeField(blank=True, null=True)),
                ('checkin_time', models.DateTimeField(blank=True, null=True)),
                ('checkedin_flag', models.BooleanField(default=False)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkedout_device', to='inventory.Device')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('inventory.device',),
        ),
    ]
