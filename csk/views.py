from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def dhoni(request):
    return HttpResponse('<marquee><h1>Thala for a reason</h1></marquee>')