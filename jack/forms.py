from django import forms
from django.forms import ModelForm, RadioSelect

from .models import *
from location.models import L_Building, L_Room

class JackForm(forms.ModelForm):
    #CHOICES = [(True, 'Acive'), (False, 'Inactive')]
    #portstatus = forms.BooleanField(widget=RadioSelect(choices=CHOICES))

    class Meta:
        model = Jack
        fields = '__all__'

class RoomForm(forms.ModelForm):
    
    class Meta:
        model = L_Room
        fields = ('number',)

class BuildingForm(forms.ModelForm):
    
    class Meta:
        model = L_Building
        fields = ('name',)
"""
class SwapForm(forms.ModelForm):

    class Meta:
        model = SwapModel
        fields = '__all__'
"""