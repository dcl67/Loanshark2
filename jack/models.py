from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

from location.models import L_Room, L_Building

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=100, blank=True, null=True)
    building = models.ForeignKey('location.L_Building', related_name='none', blank=True, null=True)

    def __str__(self):
        return self.number


class JackType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class WallplatePort(models.Model):
    """Jack position in the wall plate"""
    number = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']


class Jack(models.Model):
    wallplateport = models.ForeignKey('WallplatePort', blank=True, null=True) # 1,2,3,4
    #in_plate_type = models.ForeignKey('InPlateType', related_name='in_plate_type', blank=True, null=True)
    jack_data_type = models.ForeignKey('JackType', related_name='jack_type', blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    phone_extension = models.CharField(max_length=100, blank=True, null=True)
    port_status = models.ForeignKey('Status', related_name='active', blank=True, null=True)
    #can this information be pulled from the other corresponsing models?
    #building = models.ForeignKey('Building', related_name='jack_building', blank=True, null=True)
    #room = models.ForeignKey('Room', related_name='jack_room', blank=True, null=True)
    plate_number = models.ForeignKey('Plate', related_name='jack_plate', blank=True, null=True) #101082 plate

    def __str__(self):
        return self.plate_number.number + "-" + self.wallplateport.number + ' belonging to ' + self.display_name + ': ' + self.port_status.name


class Plate(models.Model):
    number = models.CharField(max_length=50, blank=True, null=True)
    building = models.ForeignKey('location.L_Building', related_name='foreignkey_buildig', blank=True, null=True)
    room = models.ForeignKey('location.L_Room', related_name='foreignkey_room', blank=True, null=True)
    jack = models.ManyToManyField(Jack)

    def __str__(self):
        return self.number


class Status(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.name
