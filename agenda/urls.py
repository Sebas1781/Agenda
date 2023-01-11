from django.urls import path
from . import views


urlpatterns = [
   
    path("contactos", views.contactos),
    path("menu", views.menu),
    path("", views.menu),
    path("editar", views.editar),
    path('editar/<int:id_contacto>', views.editar)
]
