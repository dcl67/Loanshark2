from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from datetime import datetime
from django.core.urlresolvers import reverse_lazy


from models import Rental, Checkout_History
from forms import RentalForm

def current_checkouts(request):
    rentals = Rental.objects.filter(checkedin_flag= False)
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

class checkout_detail(DetailView):
    model = Rental
    form = RentalForm
    
    def get_context_data(self, **kwargs):
        context = super(checkout_detail, self).get_context_data(**kwargs)
        return context

def checkin(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.checkedin_flag = True
    rental.checkin_time = datetime.now()
    record = Checkout_History.objects.create(
        device=rental.device,
        user=rental.user,
        checkout_time=rental.checkout_time,
        checkin_time=rental.checkin_time,
        checkedin_flag=True
    )
    Rental.objects.filter(pk=pk).delete()
    #rental.delete()
    print('Object should be deleted now')
    return HttpResponseRedirect(reverse('/'))

def checkout(request, pk):
    rental = Rental.objects.create(
        device=Device.objects.get(pk=pk),
        user=request.user.id,
        #checkout_time=rental.checkout_time,
        #checkin_time=null,
        checkedin_flag=False
    )

    return HttpResponseRedirect(reverse('/inventory/index/computers/'))