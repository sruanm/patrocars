from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import requires_csrf_token
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from .models import Montadora, MontadoraForm, ModeloVeiculo, ModeloVeiculoForm, Veiculo, VeiculoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
)

def admin(req):
    return render(req, "admin.html");

class MontadoraView:

    class Create(CreateView):
        model = Montadora
        form_class = MontadoraForm
        template_name = "montadoras/montadora_form.html"
        success_url = reverse_lazy("montadoras_list")
        context_object_name = 'montadora'

    class Update(UpdateView):
        model = Montadora
        form_class = MontadoraForm
        template_name = "montadoras/montadora_form.html"
        success_url = reverse_lazy("montadoras_list")
        context_object_name = 'montadora'

    class ListAll(ListView):
        model = Montadora
        template_name = "index.html"

    class Delete(DeleteView):
        model = Montadora
        success_url = reverse_lazy('montadoras_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)
        
class ModeloVeiculoView:

    def ListAll(req: HttpRequest):
        object_list = ModeloVeiculo.objects.all().order_by("-id")
        template_name = "modelos/list_modelos.html"
        return render(req,template_name,context={"object_list":object_list})

    class Create(CreateView):
        model = ModeloVeiculo
        form_class = ModeloVeiculoForm
        template_name = "modelos/create_modelo.html"
        success_url = reverse_lazy("modelos_list")
        context_object_name = 'modelo'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['montadoras'] = Montadora.objects.all()  # Passa o queryset para o template
            return context

    class Update(UpdateView):
        model = ModeloVeiculo
        form_class = ModeloVeiculoForm
        template_name = "modelos/create_modelo.html"
        success_url = reverse_lazy("modelos_list")
        context_object_name = 'modelo'

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['montadoras'] = Montadora.objects.all()  # Passa o queryset para o template
            return context
    
    class Delete(DeleteView):
        model = ModeloVeiculo
        success_url = reverse_lazy('modelos_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)
        
class VeiculoView:

    class ListAll(ListView):
        model = Veiculo
        template_name = "veiculos/list_veiculos.html"

    class Create(CreateView):
        model = Veiculo
        form_class = VeiculoForm
        template_name = "veiculos/create_veiculo.html"
        success_url = reverse_lazy("veiculos_list")

    class Update(UpdateView):
        model = Veiculo
        form_class = VeiculoForm
        template_name = "veiculos/update_veiculo.html"
        success_url = reverse_lazy("veiculos_list")
    
    class Delete(DeleteView):
        model = Veiculo
        success_url = reverse_lazy('veiculos_list')  # Redirecionar após a exclusão

        def post(self, request, *args, **kwargs):
            return self.delete(request, *args, **kwargs)