
from django.shortcuts import render, get_object_or_404
from apps.home.models import Rodape,Empresa
from .models import Banner,Oferta,Lista_Ofertas



def ofertas(request):
    empresa = get_object_or_404(Empresa, pk=1)
    rodape = get_object_or_404(Rodape, pk=1)
    ofertas= Oferta.objects.all()
    banner = get_object_or_404(Banner, pk=1)
    lista_ofertas = Lista_Ofertas.objects.all()


    data = {
         'rodape': rodape,
         'ofertas': ofertas,
         'empresa': empresa,
         'banner': banner,
         'lista_ofertas': lista_ofertas ,


    }
    return render(request, 'ofertas.html', data)



