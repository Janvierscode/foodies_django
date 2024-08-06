from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def recipes(request):
    return HttpResponse('welocome to the recipes')