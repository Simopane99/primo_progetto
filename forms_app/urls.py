from django.contrib import admin
from django.urls import path
from . import views

app_name='forms_app'

urlpatterns= [
    path("contattaci/", views.contatti, name="contatti"),
    path("lista_contatti/", views.lista_contatti, name="lista_contatti"),
    path("modifica_contatto/<int:pk>/", views.modifica_contatto, name="modifica_contatto"),
    path("elimina_contatto/<int:pk>/", views.elimina_contatto, name="elimina_contatto")
]