from django.shortcuts import render

# Create your views here.
def bf(request):
    return render(request, 'bf_main.html')