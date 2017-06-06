from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from datetime import datetime
from django.core.urlresolvers import reverse_lazy

from inventory.models import Device
from models import Rental
from forms import *

def current_checkouts(request):
    rentals = Rental.objects.filter(checkin_time__isnull=True)
    context = {
    'rentals':rentals
    }
    return render(request, 'rental/checkedout.html', context)


def checkout_history(request):
    checkoutHistory = Rental.objects.filter(checkin_time__isnull=False)
    context = {
        'checkoutHistory':checkoutHistory
    }
    return render(request, 'rental/history.html', context)

def CheckOutView(request, pk):
    if request.method == 'GET':
        form = CheckOutForm
    else:
        if isCheckedOut(pk=pk):
            form = CheckOutForm(request.POST)
            if form.is_valid():
                
                current_device = Device.objects.get(pk=pk)
                print('Current Device %s', current_device)
                user = form.cleaned_data['user']
                Rental.objects.create(device=current_device, user=user)
                return HttpResponseRedirect('/rental/checkedout/')
        else:
            return HttpResponseRedirect('/')
    return render(request, 'inventory/edit.html', {'form':form})

def isCheckedOut(pk):
    checked_out = Rental.objects.filter(device__id=pk, checkin_time__isnull=True)
    for c in checked_out:
        print c.device
    
    print(checked_out)
    if checked_out.exists():
        print("Item checked out")
        return False
    else:
        print("Not Checked out")
        return True

class checkout_detail(DetailView):
    model = Rental
    form = RentalForm
    
    def get_context_data(self, **kwargs):
        context = super(checkout_detail, self).get_context_data(**kwargs)
        return context

def checkin(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.checkin_time = datetime.now()
    rental.save()
    return HttpResponseRedirect('/rental/checkedout')
