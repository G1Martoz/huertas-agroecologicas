from django.shortcuts import render
from django.views.generic import ListView
from .models import Huerta

def home(request):
    return render(request, 'huertas/home.html')

def huerta_list(request):
    huertas = Huerta.objects.all().order_by('-id')
    return render(request, 'huertas/huerta_list.html', {'huertas': huertas})

class HuertaListView(ListView):
    model = Huerta
    template_name = 'huertas/huerta_list.html'
    context_object_name = 'huertas'
    paginate_by = 10
    ordering = ['-id']  # Show newest huertas first

def about(request):
    return render(request, 'huertas/about.html')