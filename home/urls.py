from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^results/(?P<searchtext>[-\w]+)/$', search_for_something, name='search_for_something'),
]