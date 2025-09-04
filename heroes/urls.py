from django.urls import path
from .views import HeroListView

urlpatterns = [
    path('cbv-lista/', HeroListView.as_view(), name='cbv_lista_herois'),
]
