from django.shortcuts import render
from .models import Tema

def foro(request):
    temas = Tema.objects.all().order_by('-fecha_creacion')
    return render(request, 'foro/foro.html', {'temas': temas})

# Create your views here.
