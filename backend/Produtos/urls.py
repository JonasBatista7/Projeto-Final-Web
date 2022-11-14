from django.urls import  path
from .views import produto, Carrinho, index, produtos, adicionar, addproduto

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:pk>', produto, name='produto'),
    path('produtos', produtos, name='produto'),
    path('Carrinho', Carrinho),
    path('adicionar/', adicionar, name='adicionar'),
    path('adicionar/addproduto/', addproduto, name='addproduto'),
]