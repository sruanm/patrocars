from django.contrib import admin

from .models import Montadora, ModeloVeiculo, Veiculo

# Register your models here.

@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    ...

@admin.register(ModeloVeiculo)
class ModeloVeiculoAdmin(admin.ModelAdmin):
    ...

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    ...