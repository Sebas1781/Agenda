from django.db import models
from django.forms import ModelForm
from .models import Contacto
from django import forms


class ContactoForm(forms.ModelForm):
        
        class Meta:
            model = Contacto
            fields= ['nombre','apellidos','fecha_nacio']

   

    
