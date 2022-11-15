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
from .forms import *




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
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return HttpResponseRedirect(reverse('produtos'))
    else:
        form = ProdutoForm()
    return render(request, 'adicionar-produto.html', {'form': form})



def success(request): 
    return HttpResponse('successfully uploaded') 

def produtos(request):
    prods = Produto.objects.all()
    context = { 
        'produtos': prods
    }
    return render(request, 'produtos.html', context)

def addcarrinho(request, pk):
  if ((request.user).is_authenticated):
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
  else:
    return render(request, 'erro-page.html')



def carrinho(request):
  if ((request.user).is_authenticated):
    Cars = Carrinho.objects.filter(ID_CLIENTE = request.user, STATUS_CARRINHO = 'Pedido Realizado').last()
    Itens = Produto_Quantidade.objects.filter(ID_CARRINHO = Cars)
    context = {
        'itens': Itens
    }
    return render(request, 'carrinho.html', context)
  else:
    return render(request, 'erro-page.html')


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



def pedidos(request):
    Cars = Carrinho.objects.all()
    context = {
        'cars': Cars
    }
    return render(request, 'pedidos.html', context)

def pedido_detalhes(request, pk):
  Cars = Carrinho.objects.filter(id=pk).get()
  Itens  = Produto_Quantidade.objects.filter(ID_CARRINHO = Cars)
  context = {
    'itens': Itens
  }
  return render(request, 'pedido-detalhado.html', context)
