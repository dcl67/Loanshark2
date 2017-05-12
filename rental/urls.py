from django.conf.urls import url, include
from django.core.urlresolvers import reverse_lazy

from .views import current_checkouts, handle_checkin

urlpatterns = (
    url(r'^checkedout/$', current_checkouts, name='checkedout_list'),
    url(r'^checkin/(?P<pk>[-\w]+)/$', handle_checkin, name='handle_checkin'),
)