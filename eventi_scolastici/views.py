from django.shortcuts import render
from django.db.models import Q
from .models import Evento
import datetime

def index_eventi(request):
    return render(request,"index_eventi.html")

def view_a_eventi(request):
    eventi=Evento.objects.all()
    eventi=eventi.order_by('data')
    return render(request, "view_a_eventi.html", context={
        'eventi':eventi
    })

def view_b_eventi(request):
    eventi=Evento.objects.all()
    return render(request, "view_b_eventi.html", context={
        'eventi':eventi
    })

def view_c_eventi(request):
    somma=0
    eventi=Evento.objects.all()
    for evento in eventi:
        somma+=evento.partecipanti
    media=somma/len(eventi)
    return render(request, "view_c_eventi.html", context={
        'somma':somma,
        'media':media
    })

def view_d_eventi(request):
    eventi=Evento.objects.all()
    piu_partecipanti=eventi.order_by('-partecipanti').first()
    meno_partecipanti=eventi.order_by('partecipanti').first()

    return render(request, "view_d_eventi.html", context={
        'piu_partecipanti':piu_partecipanti,
        'meno_partecipanti':meno_partecipanti
    })