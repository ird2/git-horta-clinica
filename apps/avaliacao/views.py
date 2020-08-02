
from django.shortcuts import render, get_object_or_404
from apps.home.models import Rodape,Empresa
from .models import Banner



def avaliacao(request):
    empresa = get_object_or_404(Empresa, pk=1)
    rodape = get_object_or_404(Rodape, pk=1)
    banner= get_object_or_404(Banner, pk=1)

    data = {
         'rodape': rodape,
         'banner': banner,
         'empresa': empresa,


    }


    return render(request, 'avaliacao.html',data)
