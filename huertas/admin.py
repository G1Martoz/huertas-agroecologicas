from django.contrib import admin
from .models import Huerta

@admin.register(Huerta)
class HuertaAdmin(admin.ModelAdmin):
    list_display = ['cultivo', 'tipo_plantacion', 'propietario', 'estacion_siembra', 'estacion_cosecha']
    list_filter = ['tipo_plantacion', 'estacion_siembra', 'estacion_cosecha']
    search_fields = ['cultivo', 'propietario__username']
