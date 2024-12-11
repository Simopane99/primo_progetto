from django.shortcuts import render
import datetime

# Create your views here.
def es_if(request):
    context={
        'var1':200,
        'var2':200,
        'var3':300
    }
    return render(request, "es_if.html", context)

def if_elif_else(request):
    context={
        'var1':100,
        'var2':100.0,
        'var3':100.50,
    }
    return render(request, "if_elif_else.html", context)

def index_2app(request):
    return render(request, "index_2app.html")

def es_for(request):
    context={
        'list1':[1, datetime.date(2024, 9, 10), 'nun mollà!'],
        'list2':[1, datetime.date(2024, 11, 6), 'hai mollato!!'],
        'my_dict':{'chiave1': 'Valore 1', 'chiave2': 'Valore 2'}    
    }
    return render(request, "es_for.html", context)
