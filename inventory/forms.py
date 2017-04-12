from django import forms
from django.forms import ModelForm, RadioSelect

from models import Appliance, Camera, Device, Computer, Display, Misc_Hardware, Printer, Projector

class ApplianceForm(forms.ModelForm):
    class Meta:
        model = Appliance
        fields = '__all__'


class CameraForm(forms.ModelForm):
    class Meta:
        model = Camera
        fields = '__all__'


class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = '__all__'


#class ComputerForm(forms.)


class DisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = '__all__'


class HardwareForm(forms.ModelForm):
    class Meta:
        model = Misc_Hardware
        fields = '__all__'


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'


class ProjectorForm(forms.ModelForm):
    class Meta:
        model = Projector
        fields = '__all__'