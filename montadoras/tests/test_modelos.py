from django.test import TestCase
from django.urls import reverse, resolve
from montadoras import views, models

# Create your tests here.
class ModeloTests(TestCase):
    def test_modelos_list_is_ok(self):
        url = reverse("modelos_list")
        view = resolve(url)
        
        self.assertEqual("/modelos/", url)
        self.assertEqual(view.func, views.ModeloVeiculoView.ListAll)
        
        montadora = models.Montadora.objects.create(
            name = 'Fiat',
            avatar_url = '',
            country = 'Brazil',
            foundation_year = 1900,
        )
        
        models.ModeloVeiculo.objects.create(
            name = 'Uno',
            montadora_id = montadora,
            valor_referencia = 12000,
            motorizacao = 1.2,
            turbo = False,
            automatico = True,
        )
        
        response = self.client.get(url)
        models_context = response.context['object_list']
        self.assertEqual(len(models_context),1)
        
        
        #criar modelos aqui
        #testar o contexto que tá sendo passado
        #ver se tá retornando 404
