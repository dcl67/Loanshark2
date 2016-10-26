from django.contrib import admin

from .models import *

# Register your models here.

class JackInfoAdmin(admin.ModelAdmin):
    list_display = ('portnumber',)
    search_fields = ('portnumber',)
    ordering = ('-portnumber',)

admin.site.register(JackInfo, JackInfoAdmin)
