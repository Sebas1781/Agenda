from django.contrib import admin
from agenda.models import *

class ContactosAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellidos', 'fotografia', 'fecha_nacio']
    search_fields = ['nombre']
    list_per_page = 1

admin.site.register(Contacto, ContactosAdmin)
admin.site.register(Direccion)
admin.site.register(Telefono)