from __future__ import unicode_literals

from django.apps import AppConfig
from .models import Room, Building


class LocationConfig(AppConfig):
    name = 'location'
