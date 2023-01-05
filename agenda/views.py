#from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse


def inicio(request):
    template = get_template("base.html")

    context = {
        "titulo": "Agenda"
    }

    return HttpResponse(template.render(context), request)

def contactos(request):
    return HttpResponse("Pagina 2")