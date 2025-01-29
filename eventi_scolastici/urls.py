from django.contrib import admin
from django.urls import path
from . import views

app_name='eventi_scolastici'

urlpatterns= [
    path("view_a_eventi", views.view_a_eventi, name="view_a_eventi"),
    path("view_b_eventi", views.view_b_eventi, name="view_b_eventi"),
    path("view_c_eventi", views.view_c_eventi, name="view_c_eventi"),
    path("view_d_eventi", views.view_d_eventi, name="view_d_eventi"),
    path("", views.index_eventi, name="index_eventi")
    
]