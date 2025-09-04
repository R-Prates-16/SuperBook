from django.urls import path
from .views import *

urlpatterns = [
    path('hello/', hello_heroes, name='hello_heroes'),
    path('lista/', lista_herois, name='lista_herois'),
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]

# Rian Prates