from django.urls import path
from .views import listar_equipamentos, listar_equipamentos_disponiveis

urlpatterns = [
    path('equipamentos/', listar_equipamentos),
    path('equipamentos/disponiveis/', listar_equipamentos_disponiveis),
]