from django.urls import path
from seconda_app.views import es_if, if_elif_else, index_2app
app_name="seconda_app"
urlpatterns=[
    path('es_if', es_if, name='es_if'),
    path('if_elif_else', if_elif_else, name='if_elif_else'),
    path('index_2app', index_2app, name='index_2app'),

]
