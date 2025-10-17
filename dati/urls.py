from django.urls import path
from .views import salva_partita

urlpatterns = [
    path('salva-partita/', salva_partita, name='salva-partita'),
]
