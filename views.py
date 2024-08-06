from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# from static.places import roofs24.json, moscow_legends.json


def show_map(request):
    return render(request, 'index.html')
# Create your views here.
