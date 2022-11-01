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
        return self.name


class Carrinho(models.Model):
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    QUANTIDADE = models.IntegerField()
    ID_CLIENTE = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Pedidos(models.Model):
    ID_CARRINHO: models.ForeignKey(Carrinho, on_delete=models.DO_NOTHING)