from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, StreamingHttpResponse
from django.urls import reverse
from django.utils.six.moves import range
from django.views.generic.edit import UpdateView
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import csv

from .models import JackInfo
from .forms import JackInfoForm

# View for the jack information
def index(request):
    jacks = JackInfo.objects.all()
    context = {
        'jacks': jacks,
    }
    return render(request, 'jack/index.html', context)

#framework for creating search function
def get_queryset(self):
    result = super(JackListView, self).get_queryset()

    query = self.request.GET.get('q')
    if query:
        query_list = query.split()
        result = result.filter(
            reduce(operator.and_, (Q(building_name__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(room_number__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(port_number__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(in_plate_type__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(type__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(display_name__icontains=q) for q in query_list)) |
            reduce(operator.and_, (Q(phone_extension__icontains=q) for q in query_list)))
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
        type = form.cleaned_data['type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
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
        type = form.cleaned_data['type']
        display_name = form.cleaned_data['display_name']
        phone_extension = form.cleaned_data['phone_extension']
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
