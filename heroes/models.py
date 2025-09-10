from django.db import models

class Hero(models.Model):
    codinome = models.CharField(max_length=100)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    historia = models.TextField(blank=True, null=True)
    email_contato = models.EmailField('Email de contato', max_length=254, default="heroi@heroi.com")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.codinome

# Rian Prates 