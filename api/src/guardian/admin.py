from django.contrib import admin

from .models import Device, Entry, Plant, PlantEntry

# Register your models here.
admin.site.register(Device)
admin.site.register(Plant)
admin.site.register(Entry)
admin.site.register(PlantEntry)
