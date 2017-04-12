from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .models import *
from .forms import *

from location.models import L_Building, L_Room

def landingpage(request):
    return render(request, 'inventory/home.html', context=None)

def computer_index(request):
    computers = Computer.objects.all()
    context = {
        'computers':computers
    }
    return render(request, 'inventory/comp_index.html', context)


class computer_detail(DetailView):
    model = Computer
    form = ComputerForm
    
    def get_context_data(self, **kwargs):
        context = super(computer_detail, self).get_context_data(**kwargs)
        return context
    

class computerCreate(CreateView):
    model = Computer
    fields = ['name']

    #for mac_address in form.cleaned_data['mac_address']:
        


def computer_edit(request, pk):
    instance = get_object_or_404(Computer, pk=pk)
    form = ComputerForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        form.save()
        return HttpResponseRedirect(reverse('computer_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def display_index(request):
    displays = Display.objects.all()
    context = {
        'displays':displays
    }
    return render(request, 'inventory/display_index.html', context)


class display_detail(DetailView):
    model = Display
    form = DisplayForm
    
    def get_context_data(self, **kwargs):
        context = super(display_detail, self).get_context_data(**kwargs)
        return context


class display_create(CreateView, DetailView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','resolution','video_inputs']


class display_update(UpdateView, DetailView):
    model = Display
    form = DisplayForm
    template = 'inventory/update.html'


def display_edit(request, pk):
    instance = get_object_or_404(Display, pk=pk)
    form = DisplayForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        resolution = form.cleaned_data['resolution']
        video_inputs = form.video_inputs['video_inputs']
        form.save()
        return HttpResponseRedirect(reverse('display_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def printer_index(request):
    printers = Printer.objects.all()
    context = {
        'printers':printers
    }
    return render(request, 'inventory/printer_index.html', context)


class printer_detail(DetailView):
    model = Printer
    form = PrinterForm
    
    def get_context_data(self, **kwargs):
        context = super(printer_detail, self).get_context_data(**kwargs)
        return context


class printer_create(CreateView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','hostname','toner']


def printer_edit(request, pk):
    instance = get_object_or_404(Printer, pk=pk)
    form = PrinterForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        hostname = form.cleaned_data['hostname']
        toner = form.cleaned_data['toner']
        form.save()
        return HttpResponseRedirect(reverse('printer_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def projector_index(request):
    projectors = Projector.objects.all()
    context = {
        'projectors':projectors
    }
    return render(request, 'inventory/projector_index.html', context)


class projector_detail(DetailView):
    model = Projector
    form = ProjectorForm
    
    def get_context_data(self, **kwargs):
        context = super(projector_detail, self).get_context_data(**kwargs)
        return context


class projector_create(CreateView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','make','model','video_inputs']


def projector_edit(request, pk):
    instance = get_object_or_404(Projector, pk=pk)
    form = ProjectorForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        make = form.cleaned_data['make']
        model = form.cleaned_data['model']
        video_inputs = form.cleaned_data['video_inputs']
        return HttpResponseRedirect(reverse('projector_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def camera_index(request):
    cameras = Camera.objects.all()
    context = {
        'cameras':cameras
    }
    return render(request, 'inventory/camera_index.html', context)


class camera_detail(DetailView):
    model = Camera
    form = CameraForm
    
    def get_context_data(self, **kwargs):
        context = super(camera_detail, self).get_context_data(**kwargs)
        return context


class camera_create(CreateView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','make','model']


def camera_edit(request, pk):
    instance = get_object_or_404(Camera, pk=pk)
    form = CameraForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        make = form.cleaned_data['make']
        model = form.cleaned_data['model']
        return HttpResponseRedirect(reverse('camera_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def appliance_index(request):
    appliances = Appliance.objects.all()
    context = {
        'appliances':appliances
    }
    return render(request, 'inventory/appliance_index.html', context)


class appliance_detail(DetailView):
    model = Appliance
    form = ApplianceForm
    
    def get_context_data(self, **kwargs):
        context = super(appliance_detail, self).get_context_data(**kwargs)
        return context


class appliance_create(CreateView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','resolution','video_inputs']


def appliance_edit(request, pk):
    instance = get_object_or_404(Appliance, pk=pk)
    form = ApplianceForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        appliance_name = form.cleaned_data['appliance_name']
        return HttpResponseRedirect(reverse('appliance_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})


def misc_hardware_index(request):
    hardware = Misc_Hardware.objects.all()
    context = {
        'hardware':hardware
    }
    return render(request, 'inventory/hardware_index.html', context)


class hardware_detail(DetailView):
    model = Misc_Hardware
    form = HardwareForm
    
    def get_context_data(self, **kwargs):
        context = super(hardware_detail, self).get_context_data(**kwargs)
        return context


class hardware_create(CreateView):
    model = Computer
    fields = ['name','mac_address','issued_to','owner','ip','f_id',
        'purchase_type', 'warranty_type','notes','building_location',
        'room_location','status','hardware_name']


def hardware_edit(request, pk):
    instance = get_object_or_404(Misc_Hardware, pk=pk)
    form = HardwareForm(request.POST or None, instance=instance)
    if form.is_valid():
        name = form.cleaned_data['name']
        mac_address = form.cleaned_data['mac_address']
        issued_to = form.cleaned_data['issued_to']
        owner = form.cleaned_data['owner']
        ip = form.cleaned_data['ip']
        f_id = form.cleaned_data['f_id']
        create_date = form.cleaned_data['create_date']
        modified_date = form.cleaned_data['modified_date']
        purchase_type = form.cleaned_data['purchase_type']
        warranty_type = form.cleaned_data['warranty_type']
        notes = form.cleaned_data['notes']
        building_location = form.cleaned_data['building_location']
        room_location = form.cleaned_data['room_location']
        status = form.cleaned_data['status']
        hardware_name = form.cleaned_data['misc_hardware']
        return HttpResponseRedirect(reverse('hardware_detail', kwargs={'pk':pk}))
    return render(request, 'inventory/edit.html', {'form':form})

