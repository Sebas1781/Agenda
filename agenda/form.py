from django.db import models
from django.forms import ModelForm, DateInput, FileInput
from .models import Contacto
from django import forms


class ContactoForm(forms.ModelForm):
        
        class Meta:
            model = Contacto
            fields= ['nombre','apellidos','fecha_nacio','fotografia']
  
            widgets = {
            'fecha_nacio': DateInput(attrs={'type':'date'}),
            'fotografia': FileInput(attrs={'required':False},)          
            } 
