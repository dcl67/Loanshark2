from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django.utils.six.moves import range
from django.views.generic.edit import UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import csv

from .models import *
from .forms import *

# View for the jack information
def index(request):
    building = Building.objects.all()
    room = Room.objects.all()
    plate = Plate.objects.all()
    jack_type = JackType.objects.all()
    status = Status.objects.all()
    jacks = Jack.objects.all()
    context = {
        'building': building,
        'room': room,
        'plate': plate,
        'jack_type': jack_type,
        'status': status,
        'jacks': jacks,
    }
    return render(request, 'jack/index.html', context)

"""
def landing_page(request):
    return HttpResponse("Welcome to CCI JackTracker. You're at the landing page. Type in http://127.0.0.1/jack/ to start tracking.'")
"""
# View for updating an existing jack's info'
def EditJackInfo(request, pk):
    instance = get_object_or_404(Jack, pk=pk)
    building_instance = instance.plate_number.building # wallplate form
    room_instance = instance.plate_number.room # wallplate form
    #building_instance = get_object_or_404(L_Building, pk=pk)
    #room_instance = get_object_or_404(L_Room, pk=pk)
    form = JackForm(request.POST or None, instance=instance)
    building_form = BuildingForm(request.POST or None, instance=building_instance)
    room_form = RoomForm(request.POST or None, instance=room_instance)
    if form.is_valid():
        plate_number = form.cleaned_data['plate_number']
        wallplateport = form.cleaned_data['wallplateport']
        jack_data_type = form.cleaned_data['jack_data_type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
        port_status = form.cleaned_data['port_status']
        #building = building_form.cleaned_data['building'] # wallplate port
        #room = room_form.cleaned_data['room'] # wallplate form
        building_form.save()
        room_form.save()
        form.save()
        return HttpResponseRedirect(reverse('jack'))
    return render(request, 'jack/form.html', {'form': form, 'room_form': room_form, 'building_form': building_form})

def AddJack(request):
    form = JackForm(request.POST or None)
    building_form = BuildingForm(request.POST or None, instance=instance)
    room_form = RoomForm(request.POST or None, instance=instance)
    if form.is_valid():
        plate_number = form.cleaned_data['plate_number']
        wallplateport = form.cleaned_data['wallplateport']
        jack_data_type = form.cleaned_data['jack_data_type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
        port_status = form.cleaned_data['port_status']
        form.save()
        return HttpResponseRedirect(reverse('jack'))
    return render(request, 'jack/form.html', {'form': form})

def DeleteJack(request, id):
    Jack.objects.filter(pk=id).delete()
    return HttpResponseRedirect(reverse('jack'))

def DeleteConf(request):
    return HttpResponse("Are you sure you want to delete this jack?")

def export_to_csv(request, qs, file_name):
    '''docs'''
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

    #
    #
    #

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
