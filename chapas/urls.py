from django.urls import path
from . import views

app_name = 'chapas'

urlpatterns = [
    path('', views.home, name='home'),
    path('buscar/', views.buscar_chapa, name='buscar'),
    path('contato/<int:chapa_id>/', views.registrar_contato, name='registrar_contato'),
]
