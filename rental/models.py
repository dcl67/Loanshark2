from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models
from inventory.models import *
from location.models import L_Building, L_Room

# Create your models here.
class Rental(models.Model):
    device = models.ForeignKey(Device, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    checkout_time = models.DateTimeField(auto_now=True)
    checkin_time = models.DateTimeField(blank=True, null=True)
    checkedin_flag = models.BooleanField(default=False, blank=True) #false if device is checked out, true if checked in
    if checkedin_flag is True:
        checkin_time = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user) + ' ' + str(self.device)
        print(self.checkout_time)
        print(self.checkin_time)