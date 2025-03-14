from django.contrib import admin
from .models import Tema, Respuesta

@admin.register(Tema)
class TemaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'fecha_creacion']
    list_filter = ['categoria', 'fecha_creacion']
    search_fields = ['titulo', 'descripcion', 'autor__username']
    date_hierarchy = 'fecha_creacion'

@admin.register(Respuesta)
class RespuestaAdmin(admin.ModelAdmin):
    list_display = ['tema', 'autor', 'fecha_creacion', 'es_solucion']
    list_filter = ['es_solucion', 'fecha_creacion']
    search_fields = ['contenido', 'autor__username', 'tema__titulo']
    date_hierarchy = 'fecha_creacion'
