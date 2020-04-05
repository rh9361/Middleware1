from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome_view(request):
    print('this line is from view function')
    return HttpResponse('<h1> Cust middleware demo</h1>')
