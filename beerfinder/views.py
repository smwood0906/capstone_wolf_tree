from django.shortcuts import render
from .models import Vendor

# Create your views here.
def bf(request):
    vendors = Vendor.objects.all()
    markers = []

    for vend in vendors:
        vendor_beers = []
        address = "<h6>" + vend.address + "<br>" + vend.city + ', ' + vend.state + " " + vend.zip_code
        for ty in vend.type_set.all():
            vendor_beers.append({'bottles': str(ty.bottles), "Keg": str(ty.keg), "name": ty.beer.name})
        markers.append({"name": vend.name, "beers": vendor_beers, 'address': address, 'phone':vend.phone_number,
                        "lat": float(vend.marker.lat), "lng": float(vend.marker.lon)})
    print(markers)
    return render(request, 'bf_main.html', {"markers": markers})
