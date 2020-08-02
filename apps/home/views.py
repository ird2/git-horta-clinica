
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Empresa, Preloader_site,Rodape,Banner,Sobre,Tratamento,Videos



def home(request):
    empresa = get_object_or_404(Empresa, pk=1)
    preload=get_object_or_404(Preloader_site, pk=1)
    rodape = get_object_or_404(Rodape, pk=1)
    sobre = get_object_or_404(Sobre, pk=1)
    tratamento = get_object_or_404(Tratamento, pk=1)
    banners=Banner.objects.all()
    videos = Videos.objects.all()



    data = {
        'preload':preload,
        'empresa': empresa,
        'rodape': rodape,
        'banners': banners,
        'sobre': sobre,
        'tratamento': tratamento,
        'videos': videos,

    }


    return render(request, 'home.html', data)


def my_logout(request):
    logout(request)
    return redirect('home')
