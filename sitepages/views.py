from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

def beers(request):
    return render(request, "beers.html")

def contact(request):
    return render(request, "contact.html")

def tumor(request):
    return render(request, "tumornator.html")

def about(request):
    return render(request, "about.html")



