from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def show_phones(request):
    return render(request, 'template.html')
# Create your views here.
