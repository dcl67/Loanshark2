from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# Create your models here.

BUILDING_CHOICES = (
    ('Rush', 'UCross', 'Science Center'),
)

class BuildingName(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class JackType(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class JackInfo(models.Model):
    building_name = models.ForeignKey('BuildingName', related_name='building_name')
    room_number = models.CharField(max_length=10, blank=False)
    port_number = models.CharField(max_length=50, blank=False)
    type = models.ForeignKey('JackType', related_name='type')
    display_name = models.CharField(max_length=50, blank=True)
    phone_extension = models.CharField(max_length=10, blank=True)

    def __unicode(self):
        return self.roomnumber

# class JackForm(ModelForm):
# 	class Meta:
# 		model = JackInfo
# 		fields = ['buildingname', 'roomnumber', 'person', 'callerid', 'portnumber', 'type', 'portstatus']
#         db_table = 'jackinfo'
