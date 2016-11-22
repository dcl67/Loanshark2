from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django.utils.six.moves import range
from django.views.generic.edit import UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import csv

from .models import JackInfo, SwapModel
from .forms import JackInfoForm, SwapForm

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
        building_name = form.cleaned_data['building_name']
        room_number = form.cleaned_data['room_number']
        port_number = form.cleaned_data['port_number']
        in_plate_type = form.cleaned_data['in_plate_type']
        jack_type = form.cleaned_data['jack_type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
        active = form.cleaned_data['active']
        form.save()
        return HttpResponseRedirect(reverse('jack'))
    return render(request, 'jack/form.html', {'form': form})

def AddJack(request):
    form = JackInfoForm(request.POST or None)
    if form.is_valid():
        building_name = form.cleaned_data['building_name']
        room_number = form.cleaned_data['room_number']
        port_number = form.cleaned_data['port_number']
        in_plate_type = form.cleaned_data['in_plate_type']
        jack_type = form.cleaned_data['jack_type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
        phone_extension = form.cleaned_data['active']
        form.save()
        return HttpResponseRedirect(reverse('jack'))
    return render(request, 'jack/form.html', {'form': form})

def DeleteJack(request, id):
    JackInfo.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('jack'))

def DeleteConf(request):
    return HttpResponse("Are you sure you want to delete this jack?")

def export_to_csv(request, qs, file_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="'+file_name+'".csv"'
    writer = csv.writer(response)

    model = qs.model

    headers = []
    for field in model._meta.get_fields(): # method._meta.get_fields()
        headers.append(field.name)
    writer.writerow(headers)

    for obj in qs: # method.objects.all()
        row = []
        for field in headers:
            val = getattr(obj, field)
            if callable(val):
                val = val()
            if type(val) == unicode:
                val = val.encode("utf-8")
            row.append(val)
        writer.writerow(row)

    return response

def ExportCSV(request):
    qs = JackInfo.objects.all() # Model.objects.all
    return export_to_csv(request, qs, "jackinfo") # "filename"

def SwapView(request):
    # instance = get_object_or_404(SwapModel, pk=pk)
    form = SwapForm(request.POST or None)#, instance=instance)
    if form.is_valid():
        first_building = form.cleaned_data['first_building']
        first_one_room = form.cleaned_data['first_room']
        first_one_number = form.cleaned_data['first_number']
        first_one_extension = form.cleaned_data['first_extension']

        second_building = form.cleaned_data['second_building']
        second_room = form.cleaned_data['second_room']
        second_number = form.cleaned_data['second_number']
        second_extension = form.cleaned_data['second_extension']
        return HttpResponseRedirect(reverse('swap'))
    return render(request, 'jack/swap.html', {'form': form})
