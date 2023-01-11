from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Contacto, Direccion, Telefono
from .form import ContactoForm




def inicio(request):
    template = get_template("base.html")

    context = {

    }

    return HttpResponse(template.render(context), request)

@csrf_exempt
def contactos(request):
    template = get_template("Contacto.html")

    data = {
        'form': ContactoForm()

}

    if request.method == 'POST':
        formulario= ContactoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
        else:
            data["form"] = formulario


    return HttpResponse(template.render(data))

def menu(request):
    template = get_template("menuPrincipal.html")
    contactos = Contacto.objects.all()
    
   
    context = {
        'contactos': contactos
    }

    return HttpResponse(template.render(context), request)  

def editar(request, id_contacto):
    template = get_template("editarContacto.html")

    contactos = Contacto.objects.filter(id=id_contacto).first()
    
    
   
    context = {
        'contacto': contactos,
    }

    return HttpResponse(template.render(context), request)  


    
