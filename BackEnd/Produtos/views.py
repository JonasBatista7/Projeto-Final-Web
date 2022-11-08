from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProdutoSerializer, CarrinhoSerializer
from .models import Produto, Carrinho

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated]

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer
    permission_classes = [permissions.IsAuthenticated]