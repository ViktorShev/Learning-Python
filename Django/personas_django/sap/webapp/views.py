from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def bienvenida(request):
    return HttpResponse('Hola mundo desde Django')

def despedirse(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Numero de telefono: +7 (988) 365-18-74 Email: email@django.com')