from django.urls import path
from . import views

urlpatterns = [
    path('', views.pista_corrida, name='pista_corrida'),
    path('salvar-volta/', views.salvar_volta, name='salvar_volta'),
]
