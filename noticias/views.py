from django.shortcuts import render
from .models import Noticia

def noticias(request):
    noticias_list = Noticia.objects.all().order_by('-fecha_publicacion')
    return render(request, 'noticias/noticia.html', {'noticias': noticias_list})

# Create your views here.
