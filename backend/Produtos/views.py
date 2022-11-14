from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ProdutoSerializer, CarrinhoSerializer
from .models import Produto, Carrinho
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from decimal import Decimal




def index(request):

    produtos = Produto.objects.all()
    context = {
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def editarproduto(request, pk):
  prod = Produto.objects.get(id=pk)
  context = {
    'prod': prod,
  }
  return render(request, 'produto.html', context)


def editar(request, pk):
    prod = Produto.objects.get(id=pk)
    nomedoproduto = request.POST['nome_produto']
    VALOR = request.POST['valor']
    ESTOQUE = request.POST['estoque']
    DESCRICAO = request.POST['descricao']
    prod.NOME_PRODUTO = nomedoproduto
    prod.VALOR = Decimal(VALOR)
    prod.QUANTIDADE_ESTOQUE = ESTOQUE
    prod.DESCRICAO = DESCRICAO
    prod.save()
    return HttpResponseRedirect(reverse('produtos'))

def apagarproduto(request, pk):
  prod = Produto.objects.get(id=pk)
  prod.delete()
  return HttpResponseRedirect(reverse('produtos'))


def adicionar(request):
  return render(request, 'adicionar-produto.html')

def addproduto(request):
    NM_PRODUTO = request.POST['nome']
    VALOR = request.POST['valor']
    ESTOQUE = request.POST['estoque']
    DESCRICAO = request.POST['descricao']
    prod = Produto( NOME_PRODUTO=NM_PRODUTO, VALOR=VALOR, QUANTIDADE_ESTOQUE=ESTOQUE, DESCRICAO=DESCRICAO)
    prod.save()
    return HttpResponseRedirect(reverse('produtos'))



def produtos(request):
    prods = Produto.objects.all()
    context = {
        'produtos': prods
    }
    return render(request, 'produtos.html', context)


def Carrinhos(request):
    return render(request, 'carrinho.html')