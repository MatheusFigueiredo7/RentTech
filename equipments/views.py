from django.shortcuts import render
from django.http import JsonResponse
from .models import Equipamento

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all().values()
    return JsonResponse(list(equipamentos), safe=False)

def listar_equipamentos_disponiveis(request):
    equipamentos = Equipamento.objects.filter(status="DISPONIVEL").values()
    return JsonResponse(list(equipamentos), safe=False)