from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

from .models import JackInfo
from .forms import JackInfoForm

# View for the jack information
def index(request):
    jacks = JackInfo.objects.all()
    context = {
        'jacks': jacks,
    }
    return render(request, 'jack/index.html', context)
"""
def landing_page(request):
    return HttpResponse("Welcome to CCI JackTracker. You're at the landing page. Type in http://127.0.0.1/jack/ to start tracking.'")
"""
# View for updating an existing jack's info'
def EditJackInfo(request, pk):
    instance = get_object_or_404(JackInfo, pk=pk)
    form = JackInfoForm(request.POST or None, instance=instance)
    if form.is_valid():
        buildingname = form.cleaned_data['buildingname']
        roomnumber = form.cleaned_data['roomnumber']
        portnumber = form.cleaned_data['portnumber']
        type = form.cleaned_data['type']
        callerid = form.cleaned_data['callerid']
        phone_extension = form.cleaned_data['phone_extension']
        form.save()
        return HttpResponseRedirect(reverse('jack'))
    return render(request, 'jack/form.html', {'form': form})
"""
def AddJack(request, pk):
    
    form = JackInfoForm(request.POST or None, instance=instance)
    return render(request, 'jack/form.html', {'form': form})
"""