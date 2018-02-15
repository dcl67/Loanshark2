from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import User

from .models import Rental

class UserModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
         return obj.get_full_name()

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

class CheckOutForm(forms.ModelForm):
    user = UserModelChoiceField(queryset=User.objects.all(), required = False)
    class Meta:
        model = Rental
        fields = ('user',)
