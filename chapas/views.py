from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Chapa


def home(request):
    chapas = Chapa.objects.filter(ativo=True)[:10]
    return render(request, 'chapas/home.html', {'chapas': chapas})


def buscar_chapa(request):
    query = request.GET.get('q', '')
    resultados = Chapa.objects.filter(ativo=True)
    if query:
        resultados = resultados.filter(
            Q(nome__icontains=query) |
            Q(cidade__icontains=query) |
            Q(estado__icontains=query)
        )
    return render(request, 'chapas/resultado_busca.html', {'chapas': resultados, 'query': query})


def registrar_contato(request, chapa_id):
    chapa = get_object_or_404(Chapa, id=chapa_id)
    chapa.contador_contatos += 1
    chapa.save(update_fields=['contador_contatos'])
    return redirect(chapa.link_whatsapp())
