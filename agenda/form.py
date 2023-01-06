from django.db import models
from django.forms import ModelForm
from .models import Contacto
#from django.contrib.admin.widgets import AdminDateWidget

class FContactos(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre','apellidos', 'fotografia', 'fecha_nacio']
    
