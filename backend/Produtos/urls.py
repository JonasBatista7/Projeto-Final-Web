from django.urls import  path
from .views import editarproduto, Carrinho, index, produtos, adicionar, addproduto, editar,apagarproduto

urlpatterns = [
    path('', index, name='index'),
    path('editarproduto/<int:pk>', editarproduto, name='editarproduto'),
    path('editarproduto/editar/<int:pk>', editar, name='editar'),
    path('apagarproduto/<int:pk>', apagarproduto, name='apagarproduto'),
    path('produtos', produtos, name='produtos'),
    path('Carrinho', Carrinho),
    path('adicionar/', adicionar, name='adicionar'),
    path('adicionar/addproduto/', addproduto, name='addproduto'),
]