from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import RegistroDeVolta
import json

# Renderiza a pista e passa os 10 melhores tempos ordenados
def pista_corrida(request):
    recordes = RegistroDeVolta.objects.order_by('tempo_segundos')[:10]
    return render(request, 'race/pista.html', {'recordes': recordes})

# Recebe o tempo via POST e salva no banco de dados
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
