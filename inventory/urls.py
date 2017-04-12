from django.conf.urls import url, include


from .views import *

urlpatterns = (
    # url(r'^$', landing_page, name='') home page?
    url(r'^index/computers/$', computer_index, name='computer_index'),
    url(r'^index/computers/(?P<pk>[-\w]+)/$', computer_detail.as_view(), name='computer_detail'),
    url(r'^index/computers/edit/(?P<pk>[0-9]+)/$', computer_edit, name='computer_edit'),
    url(r'^index/computers/create/$', computerCreate.as_view(template_name='inventory/edit.html'), name='computer_create'),

    url(r'^index/printer/$', printer_index, name='printer_index'),
    url(r'^index/printer/(?P<pk>[-\w]+)/$', printer_detail.as_view(), name='printer_detail'),
    url(r'^index/printer/edit/(?P<pk>[0-9]+)/$', printer_edit, name='printer_edit'),
    url(r'^index/printer/create/$', printer_create.as_view(template_name='inventory/edit.html'), name='printer_create'),

    url(r'^index/projector/$', projector_index, name='projector_index'),
    url(r'^index/projector/(?P<pk>[0-9]+)/$', projector_detail.as_view(), name='projector_detail'),
    url(r'^index/projector/edit/(?P<pk>[0-9]+)/$', projector_edit, name='projector_edit'),
    url(r'^index/projector/create/$', projector_create.as_view(template_name='inventory/edit.html'), name='projector_create'),

    url(r'^index/display/$', display_index, name='display_index'),
    url(r'^index/display/(?P<pk>[0-9]+)/$', display_detail.as_view(), name='display_detail'),
    url(r'^index/display/edit/(?P<pk>[0-9]+)/$', display_edit, name='display_edit'),
    url(r'^index/display/create/$', display_create.as_view(template_name='inventory/edit.html'), name='display_create'),

    url(r'^index/appliance/$', appliance_index, name='appliance_index'),
    url(r'^index/appliance/(?P<pk>[0-9]+)/$', appliance_detail.as_view(), name='appliance_detail'),
    url(r'^index/appliance/edit/(?P<pk>[0-9]+)/$', appliance_edit, name='appliance_edit'),
    url(r'^index/appliance/create/$', appliance_create.as_view(template_name='inventory/edit.html'), name='display_create'),

    url(r'^index/camera/$', camera_index, name='camera_index'),
    url(r'^index/camera/(?P<pk>[0-9]+)/$', camera_detail.as_view(), name='camera_detail'),
    url(r'^index/camera/edit/(?P<pk>[0-9]+)/$', camera_edit, name='camera_edit'),
    url(r'^index/camera/create/$', camera_create.as_view(template_name='inventory/edit.html'), name='display_create'),

    url(r'^index/hardware/$', misc_hardware_index, name='hardware_index'),
    url(r'^index/hardware/(?P<pk>[0-9]+)/$', hardware_detail.as_view(), name='hardware_detail'),
    url(r'^index/hardware/edit/(?P<pk>[0-9]+)/$', hardware_edit, name='hardware_edit'),
    url(r'^index/hardware/create/$', hardware_create.as_view(template_name='inventory/edit.html'), name='display_create'),

)