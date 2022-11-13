from django.urls import  path
from .views import produto, Carrinho, index

urlpatterns = [
    path('', index, name='index'),
    path('produto/<int:pk>', produto, name='produto'),
    path('Carrinho', Carrinho),
]