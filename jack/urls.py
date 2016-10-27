from django.conf.urls import url

from .views import index, EditJackInfo

urlpatterns = (
    url(r'^$', index, name='jack'),
    url(r'^update/(?P<pk>[0-9]+)/$', EditJackInfo, name='editjack'),
)