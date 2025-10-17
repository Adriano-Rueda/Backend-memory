from django.db import models
from django.utils.timezone import localtime

class Partita(models.Model):
    punteggio_giocatore_1 = models.IntegerField()
    punteggio_giocatore_2 = models.IntegerField()
    voto_giocatore_1 = models.IntegerField(null=True, blank=True)
    voto_giocatore_2 = models.IntegerField(null=True, blank=True)
    data_salvataggio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        data_locale = localtime(self.data_salvataggio)
        return f"Partita del {data_locale.strftime('%d/%m/%Y')} delle h {data_locale.strftime('%H:%M')}"
