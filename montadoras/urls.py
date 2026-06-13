from django.urls import path, include
from .views import MontadoraView, ModeloVeiculoView, VeiculoView, admin

montadoras_routes = path('montadoras/',include(
    [
        path('criar/',MontadoraView.Create.as_view(),name='montadora_create'),
        path('editar/<int:pk>/',MontadoraView.Update.as_view(),name='montadora_put'),
        path('deletar/<int:pk>/',MontadoraView.Delete.as_view(),name='montadora_delete'),
    ]
))
    
modelos_routes = [
    path('',ModeloVeiculoView.ListAll,name='modelos_list'),
    path('criar/',ModeloVeiculoView.Create.as_view(),name='modelo_save'),
    path('editar/<int:pk>/',ModeloVeiculoView.Update.as_view(),name='modelo_put'),
    path('deletar/<int:pk>/',ModeloVeiculoView.Delete.as_view(),name='modelo_delete'),
]

veiculo_routes = [
    path('',VeiculoView.ListAll.as_view(),name='veiculos_list'),
    path('criar/',VeiculoView.Create.as_view(),name='veiculo_save'),
    path('editar/<int:pk>/',VeiculoView.Update.as_view(),name='veiculo_put'),
    path('deletar/<int:pk>/',VeiculoView.Delete.as_view(),name='veiculo_delete'),
]

urlpatterns = [
    path('',MontadoraView.ListAll.as_view(),name='montadoras_list'),
    path('admin/',admin,name='admin_page'),
    path('modelos/',include(modelos_routes)),
    path('veiculos/',include(veiculo_routes)),
    montadoras_routes
]  
