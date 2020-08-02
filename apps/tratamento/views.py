from django.shortcuts import render, get_object_or_404
from apps.home.models import Rodape,Empresa
from .models import Banner,Tratamento
from django.core.paginator import Paginator



def tratamentos(request):
    empresa = get_object_or_404(Empresa, pk=1)
    rodape = get_object_or_404(Rodape, pk=1)
    tratamento= Tratamento.objects.all()
    paginator=Paginator(tratamento,6)
    page=request.GET.get('page')
    tratamento=paginator.get_page(page)
    banner = get_object_or_404(Banner, pk=1)


    data = {
         'rodape': rodape,
         'tratamentos': tratamento,
         'empresa': empresa,
         'banner': banner,


    }
    return render(request, 'tratamentos.html', data)

def tratamento_detail(request,id):


    empresa = get_object_or_404(Empresa, pk=1)
    rodape = get_object_or_404(Rodape, pk=1)
    tratamento= Tratamento.objects.get(id=id)
    banner = get_object_or_404(Banner, pk=1)
    todos_tratamentos = Tratamento.objects.all()


    data = {
         'rodape': rodape,
         'tratamentos': tratamento,
         'empresa': empresa,
         'banner': banner,
         'todos_tratamentos':todos_tratamentos,


    }
    return render(request, 'detalhe_tratamento.html', data)