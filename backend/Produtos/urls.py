from django.urls import  path
from .views import editarproduto, carrinho, index, produtos, adicionar, addproduto, editar,apagarproduto, addcarrinho, editarcarrinho, editar_item_carrinho,apagar_item_carrinho,finalizar_carrinho

urlpatterns = [
    path('', index, name='index'),
    path('editarproduto/<int:pk>', editarproduto, name='editarproduto'),
    path('editarproduto/editar/<int:pk>', editar, name='editar'),
    path('apagarproduto/<int:pk>', apagarproduto, name='apagarproduto'),
    path('produtos', produtos, name='produtos'),
    path('Carrinho', carrinho, name='Carrinho'),
    path('adicionar/', adicionar, name='adicionar'),
    path('adicionar/addproduto/', addproduto, name='addproduto'),
    path('addcarrinho/<int:pk>', addcarrinho, name='addcarinho'),
    path('editarcarrinho/<int:pk>', editarcarrinho, name='editarcarrinho'),
    path('editarcarrinho/editar_item_carrinho/<int:pk>', editar_item_carrinho, name='editar_item_carrinho'),
    path('apagar_item_carrinho/<int:pk>', apagar_item_carrinho, name='apagar_item_carrinho'),
    path('finalizar_carrinho', finalizar_carrinho, name='finalizar_carrinho')
]