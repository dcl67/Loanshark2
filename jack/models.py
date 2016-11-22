from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# Create your models here.

class BuildingName(models.Model):
    name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.name

class JackType(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class InPlateType(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class Active(models.Model):
    name = models.CharField(max_length=3, blank=True)

    def __str__(self):
        return self.name

class JackInfo(models.Model):
    building_name = models.ForeignKey('BuildingName', related_name='building_name', blank=True, null=True)
    room_number = models.CharField(max_length=100, blank=True, null=True)
    port_number = models.CharField(max_length=100, blank=True, null=True)
    in_plate_type = models.ForeignKey('InPlateType', related_name='in_plate_type', blank=True, null=True)
    jack_type = models.ForeignKey('JackType', related_name='jack_type', blank=True, null=True)
    display_name = models.CharField(max_length=100, blank=True, null=True)
    phone_extension = models.CharField(max_length=100, blank=True, null=True)
    active = models.ForeignKey('Active', related_name='active', blank=True, null=True)

class SwapModel(models.Model):
    first_building = models.ForeignKey('BuildingName', related_name='+')
    first_room = models.CharField(max_length=10, blank=False)
    first_number = models.CharField(max_length=10, blank=False)
    first_extension = models.CharField(max_length=10, blank=False)

    second_building = models.ForeignKey('BuildingName', related_name='+')
    second_room = models.CharField(max_length=10, blank=False)
    second_number = models.CharField(max_length=10, blank=False)
    second_extension = models.CharField(max_length=10, blank=False)

# class CreateJack(models.Model):
#     JackInfo.objects.create()
