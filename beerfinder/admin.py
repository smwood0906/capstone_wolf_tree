from django.contrib import admin
from .models import Vendor, Marker, Beer, Type

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Marker)
admin.site.register(Beer)
admin.site.register(Type)