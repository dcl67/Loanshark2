from django import forms
from django.forms import ModelForm, RadioSelect

from .models import JackInfo, SwapModel

class JackInfoForm(forms.ModelForm):
    #CHOICES = [(True, 'Acive'), (False, 'Inactive')]
    #portstatus = forms.BooleanField(widget=RadioSelect(choices=CHOICES))

    class Meta:
        model = JackInfo
        fields = '__all__'

class SwapForm(forms.ModelForm):

    class Meta:
        model = SwapModel
        fields = '__all__'
