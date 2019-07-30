from django.shortcuts import render
from django.http import HttpResponse

def myView(request): 
    return HttpResponse('<h1>Hello World</h1> <br> <input type="text">')
