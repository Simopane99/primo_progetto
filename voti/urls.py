from django.urls import path
from . import views

app_name="voti"
urlpatterns = [
    path('', views.index_voti, name='index_voti'),
    path('view_a/', views.view_a, name='view_a'),
    path('view_b/', views.view_b, name='view_b'),
    path('view_c/', views.view_c, name='view_c'),
    path('view_d/', views.view_d, name='view_d'),
]