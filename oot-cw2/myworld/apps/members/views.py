from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.urls import reverse

def index(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render())

def book(request):
    template = loader.get_template('BOOK.html')
    return HttpResponse(template.render())

def eraser(request):
    template = loader.get_template('eraser.html')
    return HttpResponse(template.render())

def glue(request):
    template = loader.get_template('glue.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def pen(request):
    template = loader.get_template('PEN.html')
    return HttpResponse(template.render())

def remove(request):
    template = loader.get_template('remove.html')
    return HttpResponse(template.render())

def scissors(request):
    template = loader.get_template('scissors.html')
    return HttpResponse(template.render())

def search(request):
    template = loader.get_template('search.html')
    return HttpResponse(template.render())

def back(request):
    return HttpResponseRedirect(reverse('main'))

