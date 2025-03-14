from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'precio', 'stock', 'disponible', 'vendedor']
    list_filter = ['categoria', 'disponible', 'fecha_creacion']
    search_fields = ['nombre', 'descripcion', 'vendedor__username']
    date_hierarchy = 'fecha_creacion'