from django import forms
from django.forms import ModelForm, RadioSelect

from .models import JackInfo


class JackInfoForm(forms.ModelForm):
    #CHOICES = [(True, 'Acive'), (False, 'Inactive')]
    #portstatus = forms.BooleanField(widget=RadioSelect(choices=CHOICES))


    class Meta:
        model = JackInfo
        fields = '__all__'

