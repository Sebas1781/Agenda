from django.db import models
from django.forms import ModelForm, DateInput, FileInput
from .models import Contacto, Direccion, Telefono
from django import forms


class ContactoForm(forms.ModelForm):
        
        class Meta:
            model = Contacto
            fields= '__all__'
  
            widgets = {
            'fecha_nacio': DateInput(attrs={'type':'date'}),
            'fotografia': FileInput(attrs={'required':False},)          
            } 

class DireccionForm(forms.ModelForm):
        class Meta:
            model = Direccion
            fields= '__all__'

            widgets = {
                
            }