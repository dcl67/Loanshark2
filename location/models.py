from __future__ import unicode_literals

from django.db import models


class L_Building(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class L_Room(models.Model):
    number = models.CharField(max_length=100, blank=True, null=True)
    building = models.ForeignKey('L_Building', related_name='building_room', blank=True, null=True)

    def __str__(self):
        return self.number