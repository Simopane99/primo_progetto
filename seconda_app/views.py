from django.shortcuts import render

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