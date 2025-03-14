from django.contrib import admin
from .models import Noticia

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'categoria', 'fecha_publicacion', 'destacada']
    list_filter = ['categoria', 'destacada', 'fecha_publicacion']
    search_fields = ['titulo', 'contenido', 'autor__username']
    date_hierarchy = 'fecha_publicacion'
