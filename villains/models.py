from django.db import models

class Villain(models.Model):
    codinome = models.CharField(max_length=100)
    nome_real = models.CharField(max_length=100, blank=True, null=True)
    poder_principal = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    historia = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Villain'
        verbose_name_plural = 'Villains'

    def __str__(self):
        return self.codinome
