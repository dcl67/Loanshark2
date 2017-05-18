from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy

from .views import current_checkouts, handle_checkin, checkout_history

urlpatterns = (
    url(r'^checkedout/$', current_checkouts, name='checkedout_list'),
    url(r'^history/$', checkout_history, name='checkout_history'),
    url(r'^checkout/(?P<pk>[-\w]+)/$', checkout, name='checkout'),
    url(r'^checkin/(?P<pk>[-\w]+)/$', checkin, name='checkin'),
)