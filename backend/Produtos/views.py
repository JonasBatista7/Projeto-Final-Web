from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework import permissions, authentication
from .serializers import ProdutoSerializer, CarrinhoSerializer
from .models import Produto, Carrinho, Produto_Quantidade
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
    NM_PRODUTO = request.POST['nome_produto']
    VALOR = Decimal(request.POST['valor'])
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

def addcarrinho(request, pk):
    if (Carrinho.objects.filter(ID_CLIENTE=request.user, STATUS_CARRINHO='Pedido Realizado').last()):
        car = Carrinho.objects.get(ID_CLIENTE = request.user, STATUS_CARRINHO = 'Pedido Realizado')
        prod = Produto.objects.get(id=pk)   
        SUB_TOTAL = Produto.objects.filter(id=pk).values_list('VALOR')
        Produto_Quantidade.objects.create(ID_PRODUTO = prod, ID_CARRINHO = car, QUANTIDADE = 1, SUB_TOTAL = SUB_TOTAL)
    else:
        car = Carrinho.objects.create(NOME_CARRINHO="Carrinho", ID_CLIENTE = request.user)
        prod = Produto.objects.get(id=pk)
        SUB_TOTAL = Produto.objects.filter(id=pk).values_list('VALOR')
        Produto_Quantidade.objects.create(ID_PRODUTO = prod, ID_CARRINHO = car, QUANTIDADE = 1, SUB_TOTAL=SUB_TOTAL)
    return HttpResponseRedirect(reverse('Carrinho'))



def carrinho(request):
    Cars = Carrinho.objects.filter(ID_CLIENTE = request.user, STATUS_CARRINHO = 'Pedido Realizado').last()
    Itens = Produto_Quantidade.objects.filter(ID_CARRINHO = Cars)
    context = {
        'itens': Itens
    }
    return render(request, 'carrinho.html', context)


def editarcarrinho(request, pk):
  car = Carrinho.objects.get(id=pk)
  context = {
    'car': car,
  }
  return render(request, 'editar-item-carrinho.html', context)


def editar_item_carrinho(request, pk):
    car = Carrinho.objects.get(id=pk)
    QUANTIDADE = request.POST['quantidade']
    SUB_TOTAL = int(QUANTIDADE) * (car.ID_PRODUTO.VALOR)
    car.QUANTIDADE = QUANTIDADE
    car.SUB_TOTAL = SUB_TOTAL
    car.save()
    return HttpResponseRedirect(reverse('Carrinho'))

def apagar_item_carrinho(request, pk):
  car = Carrinho.objects.get(id=pk)
  car.delete()
  return HttpResponseRedirect(reverse('Carrinho'))


def finalizar_carrinho(request):
    Carrinho.objects.filter(ID_CLIENTE = request.user).update(STATUS_CARRINHO = 'Pedido Confirmado')
    return HttpResponseRedirect(reverse('Carrinho')) 