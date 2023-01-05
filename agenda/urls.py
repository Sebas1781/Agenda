from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio),
    path("Contactos", views.contactos),
]
