from django.shortcuts import render
from .models import Vendor

# Create your views here.
def bf(request):
    vendors = Vendor.objects.all()
    markers = []
    for vendor in vendors:
        markers.append({"name": vendor.name, "lat": float(vendor.marker.lat), "lng": float(vendor.marker.lon)})
    return render(request, 'bf_main.html', {"markers": markers})