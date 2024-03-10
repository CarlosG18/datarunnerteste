from rest_framework import serializers
from .models import Treino_tempo, Treino, Teste

class TreinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino
        fields = '__all__'

class TreinoTempoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treino_tempo
        fields = '__all__'

class TesteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teste
        fields = '__all__'