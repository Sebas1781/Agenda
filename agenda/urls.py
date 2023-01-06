from django.urls import path
from . import views


urlpatterns = [
    path("", views.menu),
    path("contactos", views.contactos),
    path("menu", views.menu),
]
