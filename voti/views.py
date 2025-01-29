from django.shortcuts import render

materie = ["Matematica", "Italiano", "Inglese", "Storia", "Geografia"]

voti = {
    'Giuseppe Gullo': [("Matematica", 9, 0), ("Italiano", 7, 3), ("Inglese", 7, 4), ("Storia", 7, 4), ("Geografia", 5, 7)],
    'Antonio Barbera': [("Matematica", 8, 1), ("Italiano", 6, 1), ("Inglese", 9, 0), ("Storia", 8, 2), ("Geografia", 8, 1)],
    'Nicola Spina': [("Matematica", 7, 2), ("Italiano", 6, 2), ("Inglese", 4, 3), ("Storia", 8, 2), ("Geografia", 8, 2)]
}

def view_a(request):
    return render(request, 'view_a.html', {'materie': materie})

def view_b(request):
    return render(request, 'view_b.html', {'voti': voti})

def view_c(request):
    medie = {}
    for studente, lista_voti in voti.items():
        somma_voti = sum(voto for materia, voto, assenze in lista_voti)
        media = somma_voti / len(lista_voti)
        medie[studente] = media
    return render(request, 'view_c.html', {'medie': medie})

def view_d(request):
    max_voto = 0
    min_voto = 10
    materie_max = []
    materie_min = []
    studenti_max = []
    studenti_min = []

    for studente, lista_voti in voti.items():
        for materia, voto, assenze in lista_voti:
            if voto > max_voto:
                max_voto = voto
                materie_max = [materia]
                studenti_max = [studente]
            elif voto == max_voto:
                materie_max.append(materia)
                studenti_max.append(studente)

            if voto < min_voto:
                min_voto = voto
                materie_min = [materia]
                studenti_min = [studente]
            elif voto == min_voto:
                materie_min.append(materia)
                studenti_min.append(studente)

    return render(request, 'view_d.html', {'max_voto': max_voto, 'min_voto': min_voto,
                                           'materie_max': materie_max, 'materie_min': materie_min,
                                           'studenti_max': studenti_max, 'studenti_min': studenti_min})

def index_voti(request):
    return render(request, 'index_voti.html')