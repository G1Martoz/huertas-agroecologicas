from django.urls import path
from . import views

urlpatterns = [
    path('foro/', views.foro, name='foro'),
]