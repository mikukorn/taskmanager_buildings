from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get_buildings(request):
    return HttpResponse("Все здания")