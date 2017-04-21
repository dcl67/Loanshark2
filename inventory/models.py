from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Active(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class ComputerType(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Processor(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class MacAddress(models.Model):
    address = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.address

class Device(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    mac_address = models.ManyToManyField(MacAddress, blank=True, null=True)
    issued_to = models.ForeignKey(User, related_name='issued_to', blank=True, null=True)
    owner = models.ForeignKey(User, related_name='owner', blank=True, null=True)
    ip = models.CharField(max_length=20, blank=True, null=True)
    f_id = models.CharField(max_length=50, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    purchase_type = models.ForeignKey('PurchaseType', blank=True, null=True)
    warranty_type = models.ForeignKey('WarrantyType', blank=True, null=True)
    warranty_purchase_date = models.DateField()
    warranty_expiration_date = models.DateField()
    notes = models.TextField(blank=True, null=True)
    building_location = models.ForeignKey('location.L_Building', blank=True, null=True)
    room_location = models.ForeignKey('location.L_Room', blank=True, null=True)
    status = models.ForeignKey('Active', blank=True, null=True)

    def __str__(self):
        return self.name


class Display(Device): #device
    resolution = models.ForeignKey('Resolution', blank=True, null=True)
    video_inputs = models.ForeignKey('Input', blank=True, null=True)


class Resolution(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Printer(Device): #device
    hostname = models.CharField(max_length=100, blank=True, null=True)
    toner = models.ForeignKey('Toner', blank=True, null=True)


    def __str__(self):
        return self.name

class Toner(models.Model):
    make = models.CharField(max_length=300, blank=True, null=True)
    model = models.CharField(max_length=300, blank=True, null=True)
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    color = models.ManyToManyField(Color)

    def __str__(self):
        return self.make + ' ' + self.model + '-- total: ' + self.count

class PurchaseType(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class WarrantyType(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

class Computer(Device): #device
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=150, blank=True, null=True)
    processor = models.ForeignKey('Processor', blank=True, null=True)
    computer_type = models.ForeignKey('ComputerType', blank=True, null=True)
    hostname = models.CharField(max_length=150, blank=True, null=True)
    #jack = models.ForeignKey('jack.models.Jack', blank=True, null=True)

    def __str__(self):
        return self.name


class Projector(Device):
    make = models.CharField(max_length=100, blank=True, null=True,)
    model = models.CharField(max_length=150, blank=True, null=True)
    video_inputs = models.ForeignKey('Input', blank=True, null=True)

    def __str__(self):
        return self.name


class Bulbs(models.Model):
    make = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.make + ' ' + self.model + ', total count: ' + self.count


class Camera(Device):
    make = models.CharField(max_length=200, blank=True, null=True)
    model = models.CharField(max_length=200, blank=True, null=True)
    #building_location = models.ForeignKey('location.L_Building', blank=True, null=True)
    #room_location = models.ForeignKey('location.L_Room', blank=True, null=True)

    def __str__(self):
        return self.make + ' ' + self.model


class Appliance(Device): # examples are Echo360, ClearOne, AV Equipment, etc...
    applicance_name = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

class Misc_Hardware(Device): # examples are dongles,chargers, etc
    hardware_name = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.name

class Input(models.Model):
    video_input = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.video_input

class Licenses(models.Model):
    software_name = models.CharField(max_length=200, blank=True, null=True)
    product_key = models.CharField(max_length=100, blank=True, null=True)