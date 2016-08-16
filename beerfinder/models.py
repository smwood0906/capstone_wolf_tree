from geopy.geocoders import Nominatim
from django.db.models.signals import post_save
from django.db import models

class Marker(models.Model):
    name = models.CharField( max_length=255)
    lat = models.CharField( max_length=255)
    lon = models.CharField( max_length=255)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField( max_length=128)
    city = models.CharField( max_length=64, default="Seal Rock")
    state = models.CharField( max_length=2, default="OR")
    zip_code = models.CharField(max_length=5, default="97376")
    marker = models.ForeignKey(Marker,null= True, blank = True)

    def __str__(self):
        return self.name


# Create instances of each beer to be associated with locations
class Beer(models.Model):
    name = models.CharField(max_length=50)
    bottles = models.BooleanField(default=0)
    keg = models.BooleanField(default=0)
    vendor = models.ManyToManyField(Vendor)

    def __str__(self):
        return self.name

def lat_lon_save(sender, instance, created, **kwargs):
    if created:
        geolocator = Nominatim()
        location = geolocator.geocode(str(instance.address))

        marker = Marker()
        try:

            marker.lat = location.latitude
            marker.lon = location.longitude
        except AttributeError:
            marker.lat = "Location Error."
            marker.lon = "Location Error"
        marker.name = instance.name
        marker.save()
        instance.marker = marker
        instance.save()

post_save.connect(lat_lon_save, sender=Vendor)