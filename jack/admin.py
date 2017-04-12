from django.contrib import admin

from .models import *

# Register your models here.
"""
class JackInfoAdmin(admin.ModelAdmin):
    list_display = ('building', 'room', 'plate_number')
    search_fields = ('building', 'room', 'plate_number')
    ordering = ('plate_number',)
"""
#admin.site.register(SwapModel)

admin.site.register(Jack)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(JackType)
admin.site.register(Plate)
admin.site.register(Status)
admin.site.register(WallplatePort)
