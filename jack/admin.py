from django.contrib import admin

from .models import *

# Register your models here.

class JackInfoAdmin(admin.ModelAdmin):
    list_display = ('building_name', 'room_number', 'port_number')
    search_fields = ('building_name', 'room_number', 'port_number')
    ordering = ('port_number',)

admin.site.register(SwapModel)

admin.site.register(JackInfo, JackInfoAdmin)
admin.site.register(BuildingName)
admin.site.register(JackType)
admin.site.register(InPlateType)
admin.site.register(Active)
