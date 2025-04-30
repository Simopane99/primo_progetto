from django.urls import path
from .views import todos_view, spotify

app_name="api"

urlpatterns = [
path('todos/', todos_view, name='todos'), 
path('spotify/', spotify, name='spotify'), 
]