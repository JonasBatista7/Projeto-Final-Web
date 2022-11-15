from django.urls import  path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('editarproduto/<int:pk>', editarproduto, name='editarproduto'),
    path('editarproduto/editar/<int:pk>', editar, name='editar'),
    path('apagarproduto/<int:pk>', apagarproduto, name='apagarproduto'),
    path('produtos', produtos, name='produtos'),
    path('Carrinho', carrinho, name='Carrinho'),
    path('adicionar/', adicionar, name='adicionar'),
    path('addcarrinho/<int:pk>', addcarrinho, name='addcarinho'),
    path('editarcarrinho/<int:pk>', editarcarrinho, name='editarcarrinho'),
    path('editarcarrinho/editar_item_carrinho/<int:pk>', editar_item_carrinho, name='editar_item_carrinho'),
    path('apagar_item_carrinho/<int:pk>', apagar_item_carrinho, name='apagar_item_carrinho'),
    path('finalizar_carrinho', finalizar_carrinho, name='finalizar_carrinho'),
    path('success', success, name = 'success'),
    path('pedidos', pedidos, name = 'pedidos'),
    path('pedidos/<int:pk>', pedido_detalhes, name='pedido_detalhado')
]