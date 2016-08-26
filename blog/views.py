from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def news_main(request):
    return render(request, 'news_main.html')