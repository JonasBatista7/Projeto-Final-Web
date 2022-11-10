from .models import Produto, Carrinho
from rest_framework import serializers

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'NOME_PRODUTO', 'CREATED_BY', 'VALOR', 'QUANTIDADE_ESTOQUE', 'DESCRICAO']


class CarrinhoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['id', 'NOME_CARRINHO', 'ID_PRODUTO', 'QUANTIDADE', 'ID_CLIENTE', 'STATUS_CARRINHO']