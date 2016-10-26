from __future__ import unicode_literals
from django.db import models
from django.forms import ModelForm

# Create your models here.

BUILDING_CHOICES = (
    ('Rush', 'UCross', 'Science Center'),
)

class JackInfo(models.Model):
    buildingname = models.CharField(max_length=50) #BUILDING_CHOICES)
    roomnumber = models.CharField(max_length=10)
    person = models.CharField(max_length=50)
    callerid = models.CharField(max_length=50)
    portnumber = models.CharField(max_length=50)
    portstatus = models.BooleanField(default=False)
    

    #def __str__(self):              # __unicode__ on Python 2
        #return self.jacks.buildingname + ' ' + self.roomnumber
"""
class Room(models.Model):
    roomnumber = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.roomnumber

class DisplayName(models.Model):
    person = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.person

class CallerID(models.Model):
    callerid = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.callerid
    	
class PortNum(models.Model):
    portnumber = models.CharField(max_length=100)
    
    def __str__(self):
    	return self.portnumber

class PortActive(models.Model):
    portactive = models.CharField(max_length=100)
    #authors = models.ManyToManyField(Author)

	def __str__(self):
    	return self.portactive
"""

class JackForm(ModelForm):
	class Meta:
		model = JackInfo
		fields = ['buildingname', 'roomnumber', 'person', 'callerid', 'portnumber', 'portstatus']
        db_table = 'jackinfo'

