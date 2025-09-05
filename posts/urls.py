from django.urls import path
from . import views

urlpatterns = [
    path('lista/', views.lista_posts, name='lista_posts'),
    path('novo/', views.criar_post, name='criar_post'),  # nova rota para criar posts
]


#Rian Prates