from django.urls import path
from .views import *

urlpatterns = [
    
    path('', inicio, name='inicio'),
    path('casas/', casas, name='casas'),
    path('departamentos/', departamentos, name='departamentos'),
    path('contactos/', contactos, name='contactos'),
    path('resultadosalquiler/', buscaralquiler, name='buscaralquiler'),
    path('resultadoscasa/', buscarcasa, name='buscarcasa'),

]
