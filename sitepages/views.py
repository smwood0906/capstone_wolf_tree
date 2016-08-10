from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("WolfTree Home Page")

def beers(request):
    return HttpResponse("Beer description page")
