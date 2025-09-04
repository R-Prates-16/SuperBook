from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView

# Create your views here.
def lista_posts(request):
    posts = Post.objects.all()  # busca todos os heróis do banco
    return render(request, "posts/lista_posts.html", {"posts": posts})

class PostListView(ListView):
    model = Post
    template_name = "posts/lista_posts.html"
    context_object_name = "posts"
