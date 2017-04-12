from django.contrib import admin

from .models import L_Building, L_Room
# Register your models here.
admin.site.register(L_Building)
admin.site.register(L_Room)