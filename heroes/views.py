from django.shortcuts import render, redirect
from .forms import HeroForm
from .models import Hero  # importa o modelo

def criar_heroi(request):
    if request.method == "POST":
        form = HeroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_herois')  # redireciona para a lista
    else:
        form = HeroForm()

    return render(request, "heroes/form_heroi.html", {"form": form})


def lista_herois(request):
    herois = Hero.objects.all()
    return render(request, "heroes/lista_herois.html", {"herois": herois})

# Rian Prates