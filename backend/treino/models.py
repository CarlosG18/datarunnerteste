from django.db import models

class Treino_tempo(models.Model):
    id = models.IntegerField(primary_key=True)
    tempo_real = models.CharField(max_length=100)
    tempo_exato = models.CharField(max_length=100)
    descricao = models.CharField(max_length=100)

# Create your models here.
class Treino(models.Model):
    titulo = models.CharField(max_length=200)

class Teste(models.Model):
    title = models.CharField(max_length=200)
    dados = models.TextField()