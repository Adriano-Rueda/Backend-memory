from rest_framework import serializers
from .models import Partita

class PartitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partita
        fields = '__all__'
