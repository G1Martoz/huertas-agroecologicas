from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('huertas/', views.huerta_list, name='huerta-list'),
    path('acerca-de/', views.about, name='acerca-de'),
]