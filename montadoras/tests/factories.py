from django.test import TestCase
from django.urls import reverse, resolve
from montadoras import views, models
from typing import TypedDict

class ModeloParams(TypedDict):
  name = str
  montadora_id = models.ForeignKey(Montadora,on_delete=models.CASCADE)
  valor_referencia = models.FloatField()
  motorizacao = models.FloatField()
  turbo = models.BooleanField()
  automatico = models.BooleanField()
  
class ModeloFactory():
    
    return models.ModeloVeiculo.objects.create(
        name = 'Uno',
        montadora_id = montadora,
        valor_referencia = 12000,
        motorizacao = 1.2,
        turbo = False,
        automatico = True,
    )