from .models import Produto, Carrinho
from rest_framework import serializers

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['NOME_PRODUTO', 'CREATED_BY', 'VALOR', 'QUANTIDADE_ESTOQUE', 'DESCRICAO']


class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['NOME_CARRINHO', 'ID_PRODUTO', 'QUANTIDADE', 'ID_CLIENTE', 'STATUS_CARRINHO']