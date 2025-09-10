from django.contrib import admin
from .models import Villain

@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'criado_em']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações', {
            'fields': ('poder_principal', 'cidade', 'historia')
        }),
        ('Registro', {
            'fields': ('criado_em',)
        }),
    )

    readonly_fields = ['criado_em']


# Rian Prates