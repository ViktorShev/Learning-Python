from personas.forms import PersonaForm, DomicilioForm
from personas.models import Domicilio, Persona
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory


#////////////////////////////////////////////////////////////////////////////PERSONAS//////////////////////////////////////////////////////////////////////////////////////


def detallePersona(request, id):
    #persona = Persona.objects.get(pk=id)
    persona = get_object_or_404(Persona, pk=id)
    return render(request, 'personas/detalle.html', {'persona': persona})

#PersonaForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else: 
        formaPersona = PersonaForm()
        
    return render(request, 'personas/nuevo.html', {'formaPersona': formaPersona})

def editarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST, instance=persona)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('inicio')
    else: 
        formaPersona = PersonaForm(instance=persona)
        
    return render(request, 'personas/editar.html', {'formaPersona': formaPersona})

def eliminarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('inicio')


#////////////////////////////////////////////////////////////////////////////FIN PERSONAS//////////////////////////////////////////////////////////////////////////////////




#////////////////////////////////////////////////////////////////////////////DOMICILIOS///////////////////////////////////////////////////////////////////////////////////


def detalleDomicilio(request, id):
    #persona = Persona.objects.get(pk=id)
    domicilio = get_object_or_404(Domicilio, pk=id)
    return render(request, 'domicilios/detalleDomicilio.html', {'domicilio': domicilio})

def nuevoDomicilio(request):
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('inicio')
    else: 
        formaDomicilio = DomicilioForm()
        
    return render(request, 'domicilios/nuevoDomicilio.html', {'formaDomicilio': formaDomicilio})

def editarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('inicio')
    else: 
        formaDomicilio = DomicilioForm(instance=domicilio)
    
    return render(request, 'domicilios/editarDomicilio.html', {'formaDomicilio': formaDomicilio})
    
def eliminarDomicilio(request, id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('inicio')


#////////////////////////////////////////////////////////////////////////////FIN DOMICILIOS//////////////////////////////////////////////////////////////////////////////