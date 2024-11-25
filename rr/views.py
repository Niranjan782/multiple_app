from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sanju(request):
    return HttpResponse('<marquee><h1>Malayaliii daa mone!!!</h1></marquee>')
