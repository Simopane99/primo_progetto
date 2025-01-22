from django.shortcuts import render, get_object_or_404

from django.db.models import Q
from .models import Articolo, Giornalista
import datetime

"""
def home(request):
    a=""
    g=""
    for art in Articolo.objects.all():
        a+=(art.titolo+"<br>")

    for gio in Giornalista.objects.all():
        g+=(gio.nome+"<br>")
    response="Articoli.<br>"+ a+ "<br>Giornalisti:<br>"+ g

    return HttpResponse("<h1>"+response+"</h1>")"""

def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "homepage.html", context)

def articoloDetailView(request,pk):
    #articolo=Articolo.objects.get(pk=pk)
    articolo=get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render(request, "articolo_detail.html", context)

def index_news(request):
    return render(request,"index_news.html")

def listaArticoli(request, pk=None):
    if(pk==None):
        articoli=Articolo.objects.all() 
    
    else:
        articoli=Articolo.objects.filter(giornalista_id=pk) #filtra solo chi possiede l'id ugaule a 1
    print(articoli)
    context={
        'articoli':articoli,
    }
    return render(request,'lista_articoli.html', context)

def queryBase(request):
    #1. Tutti gli articoli scritti da giornalisti di un certo cognome:
    articoli_cognome=Articolo.objects.filter(giornalista__cognome='Rossi')
    #2. totale
    numero_totale_articoli=Articolo.objects.count()
    #3. Contare il numero di articoli scritti da un giornalista specifico:
    giornalista_1=Giornalista.objects.get(id=2)
    numero_articoli_giornalista_1=Articolo.objects.filter(giornalista=giornalista_1).count()
    #4. Ordinare gli articoli per numero di visualizzazioni in ordine decrescente:
    articoli_ordinati=Articolo.objects.order_by('-visualizzazioni')
    #5. Tutti gli articoli che non hanno visualizzazioni:
    articoli_senza_visualizzazioni=Articolo.objects.filter(visualizzazioni=0)
    #6. articolo più visualizzato 
    articolo_piu_visualizzato=Articolo.objects.order_by('-visualizzazioni').first()
    #7. Tutti i giornalisti nati dopo una certa data:
    giornalisti_data=Giornalista.objects.filter(anno_di_nascita__gt=datetime.date(1990,1,1))
    #8. Tutti gli articoli pubblicati in una data specifica:
    articoli_del_giorno=Articolo.objects.filter(data=datetime.date(2023,1,1))
    #9. Tutti gli articoli pubblicati in un intervallo di date:
    articoli_periodo=Articolo.objects.filter(data__range=(datetime.date(2023,1,1), datetime.date(2023,12,31)))
    #10. Gli articoli scritti da giornalisti nati prima del 1980:
    giornalisti_nati=Giornalista.objects.filter(anno_di_nascita__lt=datetime.date(1980,1,1))
    articoli_giornalisti=Articolo.objects.filter(giornalista__in=giornalisti_nati)
    #11. Il giornalista più giovane:
    giornalista_giovane=Giornalista.objects.order_by('anno_di_nascita').first()
    #12. Il giornalista più anziano:
    giornalista_anziano=Giornalista.objects.order_by('-anno_di_nascita').first()
    #13. Gli ultimi 5 articoli pubblicati:
    ultimi=Articolo.objects.order_by('-data')[:5]
    #14. Tutti gli articoli con un certo numero di visualizzazioni:
    articoli_minime_visualizzazioni=Articolo.objects.filter(visualizzazioni__gte=100)
    #15. Tutti gli articoli che contengono una certa parola nel titolo:
    articoli_parola=Articolo.objects.filter(titolo__icontains='importante')
    #16. Articoli pubblicati in un certo mese di un anno specifico
    articoli_mese_anno= Articolo.objects.filter(data__month=1, data__year=2023)
    #17. Giornalisti con almeno un articolo con più di 100 visualizzazioni
    giornalisti_con_articoli_popolari=Giornalista.objects.filter(articoli__visualizzazioni__gte=100).distinct()
    data=datetime.date(1990,1,1)
    visualizzazioni=50
    #18. Scrivi quali articoli vengono selezionati
    articoli_con_and=Articolo.objects.filter(giornalista__anno_di_nascita__gt=data, visualizzazioni__gte=visualizzazioni)
    #19. Scrivi quali articoli vengono selezionati
    articoli_con_or=Articolo.objects.filter(Q(giornalista__anno_di_nascita__gt=data)|Q (visualizzazioni__lte=visualizzazioni))
    #20. Scrivi quali articoli vengono selezionati
    articoli_con_not=Articolo.objects.filter(~Q(giornalista__anno_di_nascita__lt=data))
    #exclude esclude tutti i valori che rispettano la condizione
    articoli_con_not=Articolo.objects.exclude(giornalista__anno_di_nascita__lt=data)


    #Creare il dizionario context
    context={
        'articoli_cognome': articoli_cognome,
        'numero_totale_articoli': numero_totale_articoli,
        'numero_articoli_giornalista_1': numero_articoli_giornalista_1,
        'articoli_ordinati': articoli_ordinati,
        'articoli_senza_visualizzazioni': articoli_senza_visualizzazioni,
        'articolo_piu_visualizzato': articolo_piu_visualizzato,
        'giornalisti_data': giornalisti_data,
        'articoli_del_giorno': articoli_del_giorno,
        'articoli_periodo': articoli_periodo,
        'articoli_giornalisti': articoli_giornalisti,
        'giornalista_giovane': giornalista_giovane,
        'giornalista_anziano': giornalista_anziano,
        'ultimi': ultimi,
        'articoli_minime_visualizzazioni': articoli_minime_visualizzazioni,
        'articoli_parola': articoli_parola,
        'articoli_mese_anno': articoli_mese_anno,
        'giornalisti_con_articoli_popolari': giornalisti_con_articoli_popolari,
        'articoli_con_and': articoli_con_and,
        'articoli_con_or': articoli_con_or,
        'articoli_con_not': articoli_con_not,
    }
    return render(request,'query.html', context)

def giornalistaDetailView(request,pk):
    #articolo=Articolo.objects.get(pk=pk)
    giornalista=get_object_or_404(Giornalista, pk=pk)
    articoli=giornalista.articoli.all()
    context={"giornalista": giornalista,
             "articoli":articoli}
    return render(request, "giornalista_detail.html", context)