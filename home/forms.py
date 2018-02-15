from django import forms
from django.forms import ModelForm, RadioSelect

from inventory.models import Device

class SearchDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = '__all__'