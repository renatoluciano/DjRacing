from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RegistroDeVolta
import json

# 1. View que renderiza a tela da pista de corrida
def pista_corrida(request):
    return render(request, 'race/pista.html')

# 2. View que recebe o tempo em segundo via POST e salva no banco
@csrf_exempt
def salvar_volta(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        volta = RegistroDeVolta.objects.create(
            veiculo=dados.get('veiculo'),
            tempo_segundos=dados.get('tempo')
        )
        return JsonResponse({'status': 'sucesso', 'id': volta.id})
    return JsonResponse({'status': 'erro'}, status=400)
