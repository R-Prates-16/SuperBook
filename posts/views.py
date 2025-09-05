from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post  # importa o modelo

def criar_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_posts')  # redireciona para a lista após salvar
    else:
        form = PostForm()

    return render(request, "posts/form_post.html", {"form": form})


def lista_posts(request):
    posts = Post.objects.all()
    return render(request, "posts/lista_posts.html", {"posts": posts})

#Rian Prates