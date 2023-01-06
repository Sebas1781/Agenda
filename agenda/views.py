from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contacto
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
        formulario= ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"  
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
