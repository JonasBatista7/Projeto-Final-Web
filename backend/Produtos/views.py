from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ProdutoSerializer, CarrinhoSerializer
from .models import Produto, Carrinho



def index(request):
    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    } 
    return render(request, 'index.html', context)

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto': prod
    }
    return render(request, 'produtos.html', context)


def Carrinhos(request):
    return render(request, 'carrinho.html')