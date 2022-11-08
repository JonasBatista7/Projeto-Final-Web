from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Produto(models.Model):
    CREATED_BY = models.ForeignKey(User , on_delete=models.DO_NOTHING)
    NOME_PRODUTO = models.CharField(max_length=30)
    VALOR = models.IntegerField()
    QUANTIDADE_ESTOQUE = models.IntegerField()
    DESCRICAO = models.CharField(max_length=100)

    def __str__(self):
        return self.NOME_PRODUTO

TIPO_STATUS = [
    ('Pedido Realizado', 'Pedido Realizado'),
    ('Pedido Confirmado', 'Pedido Confirmado'),
]

class Carrinho(models.Model):
    NOME_CARRINHO = models.CharField(max_length=30)
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    QUANTIDADE = models.IntegerField()
    ID_CLIENTE = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    STATUS_CARRINHO = models.CharField(
        max_length=40,
        choices=TIPO_STATUS,
        default='Pedido Realizado',
    )

    def __str__(self):
        return self.NOME_CARRINHO