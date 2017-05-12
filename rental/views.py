from django.shortcuts import render
import datetime

from models import Rental

def current_checkouts(request):
    rentals = Rental.objects.filter(checkedin_flag= False)
    print(rentals)
    context = {
    'rentals':rentals
    }
    return render(request, 'rental/checkedout.html', context)


def checkout_records(request):
    allCheckouts = Rental.objects.all()
    context = {
        'allCheckouts':allCheckouts
    }
    return render(request, 'rental/checkoutrecord.html', context)

#def handle_checkout(request):
#    

def handle_checkin(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.checkedin_flag = True
    rental.checkin_time = datetime.now()
    rental.save()