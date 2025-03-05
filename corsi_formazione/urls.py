from django.contrib import admin
from django.urls import path
from .views import index_corsi,view_a_corsi,view_b_corsi,view_c_corsi,view_d_corsi,view_e_corsi, corsoDetailView,view_f_corsi

app_name='corsi_formazione'

urlpatterns= [
    path("", index_corsi, name="index_corsi"),
    path("view_a_corsi", view_a_corsi, name="view_a_corsi"),
    path("view_b_corsi", view_b_corsi, name="view_b_corsi"),
    path("corso/<int:pk>", corsoDetailView, name="corsoDetailView"),
    path("view_c_corsi", view_c_corsi, name="view_c_corsi"),
    path("view_d_corsi", view_d_corsi, name="view_d_corsi"),
    path("view_e_corsi", view_e_corsi, name="view_e_corsi"),
    path("view_f_corsi", view_f_corsi, name="view_f_corsi"),
]