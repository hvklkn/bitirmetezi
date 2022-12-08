from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text="merhaba ben veli kalkan"
    return HttpResponse("Deneme Test Sayfası: %s" % text)
