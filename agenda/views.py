from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .form import FContactos
from django.views.decorators.csrf import csrf_exempt




def inicio(request):
    template = get_template("base.html")

    context = {

    }

    return HttpResponse(template.render(context), request)

@csrf_exempt
def contactos(request):
    template = get_template("Contacto.html")
    form = FContactos()

    if request.method == 'POST':
        form = FContactos(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return HttpResponse(template.render(context), request)

def menu(request):
    template = get_template("menuPrincipal.html")

    context = {
        "titulo": "Menu"
    }

    return HttpResponse(template.render(context), request)     
