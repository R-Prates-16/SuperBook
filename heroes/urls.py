from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.criar_heroi, name='criar_heroi'),
    path('', views.lista_herois, name='lista_herois'),  # rota raiz do app heroes
]


# Rian Prates