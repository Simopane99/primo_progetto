from django.shortcuts import render, get_object_or_404
from .models import Corso
import datetime

def index_corsi(request):
    return render(request,"index_corsi.html")

def view_a_corsi(request, pk):
    if(pk==None):
        corsi=Corso.objects.all() 
    
    else:
        corsi=Corso.objects.filter(corso__id=pk) 
    corsi=corsi.order_by('data_inizio')
    return render(request, "view_a_corsi.html", context={
        'corsi':corsi
    })

def view_b_corsi(request):
    corsi=Corso.objects.all()
    corsi=corsi.order_by('data_inizio')
    return render(request, "view_b_corsi.html", context={
        'corsi':corsi
    })

def corsoDetailView(request,pk):
    corso=get_object_or_404(Corso, pk=pk)
    context={"corso": corso}
    return render(request, "corsoDetailView_detail.html", context)

def view_c_corsi(request):
    corsi=Corso.objects.filter(data_inizio__gt=datetime.date(2025,5,1))
    return render(request, "view_c_corsi.html", context={
        'corsi':corsi
    })

def view_d_corsi(request):
    meno_posti=Corso.objects.filter(posti_disponibili__lt=20)
    return render(request, "view_d_corsi.html", context={
        'meno_posti':meno_posti
    })

def view_e_corsi(request):
    corsi=Corso.objects.filter(data_fine__lte=datetime.date(2025,4,30))
    return render(request, "view_e_corsi.html", context={
        'corsi':corsi
    })

def view_f_corsi(request):
    posti_totali=0
    corsi=list(Corso.objects.all())
    corso_piu_posti=Corso.objects.order_by('posti_disponibili').first()
    corso_meno_posti=Corso.objects.order_by('-posti_disponibili').first()
    for corso in corsi:
        for _,_,_,_,posti in corso:
            posti_totali+=posti
    return render(request, "view_f_corsi.html", context={
        'corso_piu_posti':corso_piu_posti,
        'corso_meno_posti':corso_meno_posti,
        'posti_totali':posti_totali
    })