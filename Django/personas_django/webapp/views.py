from django.shortcuts import render
from django.http import HttpResponse

def bienvenida(request):
    return HttpResponse('Hola mundo desde Django')

def despedida(request):
    return HttpResponse('Adiós desde Django')

def contacto(request):
    return HttpResponse('Email: mail@django.com - Num. de telefono: +79883683415')