from django.shortcuts import render

from models import Rental

def current_checkouts(request):
    if Rental.checkout_flag is True:
        checkedout = Rental.objects.all()
        print(checkedout)
        context = {
        'checkedout':checkedout
        }
    return render(request, 'rental/checkedout.html', context)


def checkout_records(request):
    allCheckouts = Rental.objects.all()
    context = {
        'allCheckouts':allCheckouts
    }
    return render(request, 'rental/checkoutrecord.html', context)

def handle_checkout(request):
    

def handle_checkin(request):
    rental = Rental.objects.get()
    rental.checkout_flag = True
