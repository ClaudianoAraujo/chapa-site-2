import os

from django.contrib import admin
from django.urls import path, include

# Caminho do admin configurável por variável de ambiente (ADMIN_URL).
# Se não definida, cai no padrão 'admin/' (recomendado trocar em produção).
ADMIN_URL = os.environ.get('ADMIN_URL', 'admin/')

urlpatterns = [
    path(ADMIN_URL, admin.site.urls),
    path('', include('chapas.urls')),
]