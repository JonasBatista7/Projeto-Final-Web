from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Produto(models.Model):
    NOME_PRODUTO = models.CharField(max_length=30,unique=True)
    VALOR = models.DecimalField(max_digits=6, decimal_places=2)
    QUANTIDADE_ESTOQUE = models.IntegerField()
    DESCRICAO = models.CharField(max_length=100)
    IMAGEM = models.ImageField(upload_to='images/', null = True)

    def __str__(self):
        return self.NOME_PRODUTO

TIPO_STATUS = [
    ('Pedido Realizado', 'Pedido Realizado'),
    ('Pedido Confirmado', 'Pedido Confirmado'),
]

class Carrinho(models.Model):
    NOME_CARRINHO = models.CharField(max_length=30, default='Carrinho')
    ID_PRODUTO = models.ManyToManyField(Produto, through='Produto_Quantidade')
    ID_CLIENTE = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    STATUS_CARRINHO = models.CharField(
        max_length=40,
        choices=TIPO_STATUS,
        default='Pedido Realizado',
    )
    def __str__(self):
        return self.NOME_CARRINHO

TIPO_USUARIO = [
    ('Cliente', 'Cliente'),
    ('Funcionario', 'Funcionario'),
    ('Administrador', 'Administrador')
]

class Produto_Quantidade(models.Model):
    ID_PRODUTO = models.ForeignKey(Produto, on_delete=models.CASCADE)
    ID_CARRINHO = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    QUANTIDADE = models.IntegerField()
    SUB_TOTAL = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "{}_{}".format(self.ID_PRODUTO.__str__(), self.ID_CARRINHO.__str__())

