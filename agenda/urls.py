from django.urls import path
from . import views


urlpatterns = [
    path("", views.inicio),
    path("contactos", views.contactos),
    path("menu", views.menu),
]
