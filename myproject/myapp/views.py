#my views
from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return HttpResponse('<h1>HELLO! WELCOME<h1>')
