from django.contrib import admin
from django.urls import path
from .views import home, articoloDetailView, index_news, listaArticoli, queryBase, giornalistaDetailView

app_name='news'

urlpatterns= [
    path("home", home, name="homepage"),
    path("lista_articoli/", listaArticoli, name="lista_articoli_giornalista"),
    path("lista_articoli/<int:pk>", listaArticoli, name="lista_articoli_giornalista"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("query", queryBase, name="query_base"),
    path("giornalisti/<int:pk>", giornalistaDetailView, name="giornalista_detail"),
    path("", index_news, name="index_news")
]