from django.contrib import admin

from .models import *

# Register your models here.

class JackInfoAdmin(admin.ModelAdmin):
    list_display = ('buildingname', 'roomnumber', 'portnumber')
    search_fields = ('buildingname', 'roomnumber', 'portnumber')
    ordering = ('portnumber',)

admin.site.register(JackInfo, JackInfoAdmin)
admin.site.register(Status)
