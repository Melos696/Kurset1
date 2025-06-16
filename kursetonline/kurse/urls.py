from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_kurseve, name='lista_kurseve'),
]
