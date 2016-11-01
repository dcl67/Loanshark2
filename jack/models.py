from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# Create your models here.

BUILDING_CHOICES = (
    ('Rush', 'UCross', 'Science Center'),
)

class Status(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class JackInfo(models.Model):
    buildingname = models.CharField(max_length=50, blank=False) #BUILDING_CHOICES)
    roomnumber = models.CharField(max_length=10, blank=False)
    portnumber = models.CharField(max_length=50, blank=False)
    type = models.CharField(max_length=20, blank=False)
    callerid = models.CharField(max_length=50, blank=True)
    phone_extension = models.CharField(max_length=10, blank=True)

    def __unicode(self):
        return self.roomnumber
# class JackForm(ModelForm):
# 	class Meta:
# 		model = JackInfo
# 		fields = ['buildingname', 'roomnumber', 'person', 'callerid', 'portnumber', 'type', 'portstatus']
#         db_table = 'jackinfo'
