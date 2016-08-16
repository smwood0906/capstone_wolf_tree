from django.contrib import admin
from .models import Vendor, Marker, Beer

# Register your models here.
admin.site.register(Vendor)
admin.site.register(Marker)
admin.site.register(Beer)