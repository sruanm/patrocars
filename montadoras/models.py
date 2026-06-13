from django.db import models
from django.forms import ModelForm

# Create your models here.

class Montadora(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  avatar_url = models.CharField(max_length=200)
  country = models.CharField(max_length=100)
  foundation_year = models.IntegerField()

  class Meta:
        ordering = ['name','foundation_year']
  def __str__(self):
    return self.name

class ModeloVeiculo(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=200)
  montadora_id = models.ForeignKey(Montadora,on_delete=models.CASCADE)
  valor_referencia = models.FloatField()
  motorizacao = models.FloatField()
  turbo = models.BooleanField()
  automatico = models.BooleanField()
  def __str__(self):
    return self.name

class Veiculo(models.Model):
  id = models.AutoField(primary_key=True)
  modelo_id = models.ForeignKey(ModeloVeiculo,on_delete=models.CASCADE)
  cor = models.CharField(max_length=150)
  ano_fabricacao = models.IntegerField()
  ano_modelo = models.IntegerField()
  valor = models.IntegerField()
  placa = models.CharField(max_length=20)
  vendido = models.BooleanField()
  def __str__(self):
    return self.cor
  
class MontadoraForm(ModelForm):
    class Meta:
        model = Montadora
        fields = ["name", "country", "foundation_year","avatar_url"]

class ModeloVeiculoForm(ModelForm):
    class Meta:
        model = ModeloVeiculo
        fields = ["name", "montadora_id", "valor_referencia","motorizacao","turbo","automatico"]

class VeiculoForm(ModelForm):
   class Meta:
        model = Veiculo
        fields = ["modelo_id", "cor", "ano_fabricacao","ano_modelo", "valor", "placa","vendido"]