from django.shortcuts import render
from django.db.models import Q
from .models import Producto

def tienda(request):
    productos = Producto.objects.filter(disponible=True)
    categorias = dict(Producto.CATEGORIA_CHOICES)

    # Filtrar por categoría
    categoria = request.GET.get('categoria')
    if categoria:
        productos = productos.filter(categoria=categoria)

    # Búsqueda de productos
    busqueda = request.GET.get('busqueda')
    if busqueda:
        productos = productos.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda)
        )

    context = {
        'productos': productos,
        'categorias': categorias,
    }
    return render(request, 'tienda/tienda.html', context)