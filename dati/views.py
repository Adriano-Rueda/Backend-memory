from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import Partita
from django.utils.timezone import now

@csrf_exempt 
def salva_partita(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            partita = Partita.objects.create(
                punteggio_giocatore_1=data.get('punteggio_giocatore_1'),
                punteggio_giocatore_2=data.get('punteggio_giocatore_2'),
                voto_giocatore_1=data.get('voto_giocatore_1'),
                voto_giocatore_2=data.get('voto_giocatore_2'),
                data_salvataggio=now()
            )
            return JsonResponse({'message': 'Partita salvata con successo!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Metodo non consentito'}, status=405)
