from django.contrib import admin
from .models import Chapa


@admin.register(Chapa)
class ChapaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', 'estado', 'telefone', 'verificado', 'contador_contatos', 'ativo', 'data_cadastro')
    list_filter = ('estado', 'verificado', 'ativo')
    search_fields = ('nome', 'cidade', 'telefone')
    list_editable = ('verificado', 'ativo')
    ordering = ('-data_cadastro',)
