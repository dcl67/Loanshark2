from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy

from .views import current_checkouts, checkin, checkout_detail, checkout_history, CheckOutView

urlpatterns = (
    url(r'^checkedout/$', current_checkouts, name='checkedout_list'),
    url(r'^checkedout/(?P<pk>[0-9]+)/$', checkout_detail.as_view(), name='checkedout_detail'),
    url(r'^history/$', checkout_history, name='checkout_history'),
    #url(r'^checkoutview', CheckOutView.as_view(), name='checkout_view'),
    url(r'^checkout/(?P<pk>[0-9]+)/$', CheckOutView, name='checkout'),
    url(r'^checkin/(?P<pk>[0-9]+)/$', checkin, name='checkin'),
)