from django.shortcuts import render
from personas.models import Persona
from django.http import HttpResponse

def bienvenida(request):
    no_personas = Persona.objects.count()
    personas = Persona.objects.all()
    return render(request, 'bienvenido.html', {
        'no_personas': no_personas,
        'personas': personas
    })