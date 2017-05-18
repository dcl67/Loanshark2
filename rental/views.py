from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime

from models import Rental, Checkout_History

def current_checkouts(request):
    rentals = Rental.objects.filter(checkedin_flag= False)
    print(rentals)
    context = {
    'rentals':rentals
    }
    return render(request, 'rental/checkedout.html', context)


def checkout_history(request):
    checkoutHistory = Checkout_History.objects.all()
    context = {
        'checkoutHistory':checkoutHistory
    }
    return render(request, 'rental/history.html', context)

#def handle_checkout(request):
#    

def checkin(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.checkedin_flag = True
    rental.checkin_time = datetime.now()
    rental.save()
    record = Checkout_History.objects.create(
        device=rental.device,
        user=rental.user,
        checkout_time=rental.checkout_time,
        checkin_time=rental.checkin_time,
        checkedin_flag=True
    )
    #record.save()
    print(record)
    #rental.delete()
    return HttpResponseRedirect(reverse('/inventory/index/computers/'))

def checkout(request, pk):
    rental = Rental.objects.create(
        device=Device.objects.get(pk=pk),
        user=request.user.id,
        #checkout_time=rental.checkout_time,
        #checkin_time=null,
        checkedin_flag=False
    )