
from django.contrib import admin
from .models import Hero

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['codinome', 'nome_real', 'poder_principal', 'cidade', 'email_contato', 'criado_em']
    list_filter = ['cidade']
    search_fields = ['codinome', 'nome_real', 'cidade']

    fieldsets = (
        ('Identidade Secreta', {
            'fields': ('codinome', 'nome_real')
        }),
        ('Informações Gerais', {
            'fields': ('poder_principal', 'cidade', 'historia', 'email_contato')
        }),
        ('Dados de Registro', {
            'fields': ('criado_em',)
        }),
    )
    readonly_fields = ['criado_em']

# Rian Prates