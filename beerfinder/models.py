from django.db import models

# Create your models here.

#Create instances of locations to store business information for database
class Vendor(models.Model):
    name = models.CharField(max_length=50)
    address_1 = models.CharField( max_length=128)

    city = models.CharField( max_length=64, default="Seal Rock")
    state = models.CharField( max_length=2, default="OR")
    zip_code = models.CharField(max_length=5, default="97376")

# Create instances of each beer to be associated with locations

class Beer(models.Model):
    name = models.CharField(max_length=50)
    bottles = models.BooleanField(default=0)
    keg = models.BooleanField(default=0)
    vendor = models.ManyToManyField(Vendor)

