from django.contrib import admin
from django.urls import path
from .views import home, articoloDetailView, index_news

app_name='news'

urlpatterns= [
    path("home", home, name="homepage"),
    path("articoli/<int:pk>", articoloDetailView, name="articolo_detail"),
    path("", index_news, name="index_news")
]